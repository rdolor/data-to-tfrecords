from datetime import datetime

import tensorflow as tf
import logging
import os


def str_to_int(list_str):
    """Convert list of string to list of int.
    Args:
        List containing string type
    Returns:
        List containing int type
    """
    try:
        return [int(item) for item in list_str]
    except:
        return [0]


def preprocess_df(filename, features, num_rows=None):
    """Read txt file and preprocess
    Args: 
        str: filename of the txt data
        int: number of rows to get from the file
    """
    import pandas as pd
    import config

    try:
        df = pd.read_csv(filename, sep="\t", nrows=num_rows)
        logging.info('df shape: rows %d cols %d', df.shape[0], df.shape[1])

        df = df[features]
        df["usertag"] = df["usertag"].astype(str).map(
            lambda x: str_to_int(x.split(",")))
        #df.fillna(0, inplace=True)

        return df

    except Exception as ex:
        logging.error("Reading data error: %s", ex, exc_info=True)


def create_logger():
    """Setup the logging environment"""
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    format_str = '%(asctime)s [%(process)d] [%(levelname)s] %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(format_str, date_format)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    log.addHandler(stream_handler)
    return logging.getLogger(__name__)


def create_filename(filetype, now, prefix="train_data_"):
    """Create the filename
    Args:
        filetype (str): What type of file that will be created.
    Returns:
        str: String of the file name that will be created.
    """
    extension = "." + filetype.lower()
    timestamp = now.strftime("%Y-%m-%dT%H:%M:%S.%f")

    file_dir = os.path.dirname(os.path.realpath(__file__))
    file_dir_filetype = file_dir + "/output"

    if not os.path.isdir(file_dir_filetype):
        os.makedirs(file_dir_filetype)

    return file_dir + "/output/" + prefix + timestamp + extension


def check_dtype(df, features, data_type):
    """Checking if data type is correct
    Args:
        pandas dataframe: containing features and values
        list of feature names
        data_type: expected data type of the set of features
    Returns:
        True or Error description
    """

    for feature in features:
        try:
            return df[feature].dtype == data_type
        except Exception as ex:
            logging.error("Data type error: %s", ex, exc_info=True)


def _int64_feature(value):
    """ Returns an int64_list from a bool / enum / int / uint."""
    return tf.train.Feature(int64_list=tf.train.Int64List(value=value))


def _float_feature(value):
    """ Returns an float_list from a bool / enum / int / uint."""
    return tf.train.Feature(float_list=tf.train.FloatList(value=value))


def write_to_tfrecords(data_df, features):
    """ Write pandas dataframe into TFRecords
    Args:
        pandas dataframe: each column is a feature
        list: list of features
    """
    import config

    tf_file = create_filename('tf', datetime.now())

    try:
        writer = tf.python_io.TFRecordWriter(tf_file)

        for _, row in data_df.iterrows():
            features = {}

            for feature in config.features_dtype_int:
                features[feature] = _int64_feature([row[feature]])
            for feature in config.features_dtype_list:
                features[feature] = _int64_feature(row[feature])

            # Create an example protocol buffer
            example = tf.train.Example(
                features=tf.train.Features(feature=features))

            # Writing the serialized example.
            writer.write(example.SerializeToString())

        writer.close()
        logging.info("TF file created. File name: " + tf_file)

    except Exception as ex:
        logging.error("Error writing TF: %s", ex, exc_info=True)


def extract_tfrecords(data_record):
    """ Extracting row(s) of TFrecord file
    Args:
        TFrecord row(s)
    Returns:
        Dictionary of tensors; each key is a feature
    """
    from data_to_tf import config
    # import config  #main.py

    features = {}
    try:
        for feature in config.all_features:
            features[feature] = tf.VarLenFeature(tf.int64)

    except Exception as ex:
        logging.error("Error feature type: %s", ex, exc_info=True)

    sample = tf.parse_single_example(data_record, features)

    for key in sample.keys():
        sample[key] = tf.reshape(tf.sparse.to_dense(sample[key]), [-1])

    return sample
