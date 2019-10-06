import tensorflow as tf
import logging
import os


def create_logger():
    """Setup the logging environment"""
    log = logging.getLogger()   # root logger
    log.setLevel(logging.INFO)
    format_str = '%(asctime)s [%(process)d] [%(levelname)s] %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(format_str, date_format)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    log.addHandler(stream_handler)
    return logging.getLogger(__name__)

def create_filename(filetype, now):
    """Create the filename
    Args:
        filetype (str): What type of file that will be created.
    Returns:
        str: String of the file name that will be created.
    """
    prefix = "train_data"
    extension = "." + filetype.lower()
    timestamp = now.strftime("%Y-%m-%dT%H:%M:%S.%f")

    file_dir = os.path.dirname(os.path.realpath(__file__))

    return file_dir + "/" + filetype.upper() + "/" + prefix + extention + timestamp + extension


def _int64_feature(value):
    """ Returns an int64_list from a bool / enum / int / uint."""
    return tf.train.Feature(int64_list=tf.train.Int64List(value=value))


def _float_feature(value):
    """ Returns an float_list from a bool / enum / int / uint."""
    return tf.train.Feature(float_list=tf.train.FloatList(value=value))


def write2TF(data):
    """ Write final formatted dict to TF files
    Args:
        dict of data (dict): responseid as key, and dict of data as value
    """
    tf_file = get_filename('tf', datetime.now())
    try:
        writer = tf.python_io.TFRecordWriter(tf_file)

        for result in final_dict:
            features = {}

            for feature in config.INT_FEATURES_LIST:
                """
                if feature == 'iab' or feature == 'ad_labels':
                    features[feature] = _int64_feature(final_dict[result][feature].reshape(-1))
                else:
                    features[feature] = _int64_feature(final_dict[result][feature])
                """
                features[feature] = _int64_feature(final_dict[result][feature])
            for feature in config.FLOAT_FEATURES_LIST:
                features[feature] = _float_feature(final_dict[result][feature])

            # Create an example protocol buffer
            example = tf.train.Example(
                features=tf.train.Features(feature=features))

            # Writing the serialized example.
            writer.write(example.SerializeToString())

        writer.close()
        logging.info("TF file created. File name: " + tf_file)
    except Exception as ex:
        logging.error("Error writing TF. %s", ex, exc_info=True)
