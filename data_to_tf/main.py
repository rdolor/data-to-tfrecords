import utils
import config

if __name__ == "__main__":
    log = utils.create_logger()

    log.info('Load and preprocess data...')
    df = utils.preprocess_df(config.filename, num_rows=config.num_rows)

    log.info('Checking features data type if same as expected...')
    utils.check_dtype(df, config.features_dtype_int, int)
    utils.check_dtype(df, config.features_dtype_list, list)

    log.info('Writing to TFRecords...')
    utils.write_to_tfrecords(df, config.all_features)

    log.info('Finished all')
