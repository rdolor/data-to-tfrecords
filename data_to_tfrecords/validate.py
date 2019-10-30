import data_to_tfrecords.config as config
import logging

INI_SECTIONS     = ["DIRECTORY"]
DIRECTORY_FIELDS = ["num_rows", "filename"]


def config_validate():
    valid = []

    # Validate sections
    section_diff = list(set(INI_SECTIONS)-set(config.INI.sections()))
    if len(section_diff) > 0:
        logging.error(
            "ini file validation 'FAIL', missing sections %s", section_diff)
        valid.append(False)

    # Validate DIRECTORY section fields
    agg_dict = dict(config.INI.items("DIRECTORY"))
    if len(agg_dict) == 0:
        logging.error(
            "ini file validation 'FAIL', missing fields 'DIRECTORY' section.")
        valid.append(False)
    for key in DIRECTORY_FIELDS:
        if key not in agg_dict:
            logging.error(
                "ini file validation 'FAIL', missing fields '%s' under 'DIRECTORY' section.", key)
            valid.append(False)

    if len(valid) > 0:
        logging.error("ini file validation 'FAIL'.")
        return False

    logging.info("ini file validation 'PASS', will start the main process.")
    return True
