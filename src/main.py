import src.config as config
import src.utils as utils
import src.validate as validate


def main():
    log = utils.create_logger()

    if validate.config_validate():
        log.info('Load and preprocess data...')

        df = utils.preprocess_df(
            filename=config.INI['DIRECTORY']['filename'],
            features=config.all_features,
            num_rows=int(config.INI['DIRECTORY']['num_rows']))

        log.info('Checking features data type if same as expected...')
        utils.check_dtype(df, config.features_dtype_int, int)
        utils.check_dtype(df, config.features_dtype_list, list)

        log.info('Writing to TFRecords...')
        utils.write_to_tfrecords(df, config.all_features)

        log.info('Finished all')


if __name__ == "__main__":
    main()
