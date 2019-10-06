import os
import pandas as pd

import utils
import config

log = utils.create_logger()
log.info('current directory: %s', os.getcwd())

data = pd.read_csv('/home/rosalie/Documents/Projects/datasets/1458/train.log.txt',sep="\t", nrows=10000)
log.info('data: rows %d cols %d', data.shape[0],data.shape[1])

data = data[config.label + config.features]

log.info(data.columns)

if __name__ == "__main__":
    pass

