from datetime import datetime
from pandas import DataFrame

import tensorflow as tf
import numpy as np
import os

from data_to_tf import utils, config


def test_create_filename():
    """Test creating training data filename"""
    filetype = 'test'
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%dT%H:%M:%S.%f")
    result = utils.create_filename(filetype, now)
    assert result == os.getcwd() + '/data_to_tf/output/train_data_' + \
        timestamp + '.test'


def test_str_to_int():
    """Test converting list of string to int"""
    list_str = ["10", "20", "30"]
    result = utils.str_to_int(list_str)
    assert result == [10, 20, 30]


def test_check_dtype():
    """Test checking of data type"""
    data = {'int1': [1, 2, 3],
            'int2': [4, 5, 6],
            'list1': [[1, 2, 3], ["a"], ["b"]],
            'float1': [1., 2., 3.]}
    df = DataFrame.from_dict(data)
    assert utils.check_dtype(df, ['int1', 'int2'], int) == True
    assert utils.check_dtype(df, ['list1'], list) == True
    assert utils.check_dtype(df, ['float1'], float) == True


def test_extract_TFrecords():
    tf_file_dir = os.getcwd() + '/data_to_tf/test/data/data_to_test.tf'
    batch_size = 100

    input_padded_shapes = {}
    for feature in config.all_features:
        input_padded_shapes[feature] = [None]

    input_padding_values = {}
    for feature in config.all_features:
        input_padding_values[feature] = tf.constant(-1, dtype=tf.int64)

    dataset = tf.data.TFRecordDataset(tf_file_dir)
    dataset = dataset.map(utils.extract_tfrecords, num_parallel_calls=4)
    dataset = dataset.padded_batch(batch_size,
                                   padded_shapes=input_padded_shapes,
                                   padding_values=input_padding_values)

    iterator = dataset.make_one_shot_iterator()
    next_batch = iterator.get_next()

    with tf.Session() as sess:
        batch = sess.run(next_batch)
        for feature in config.all_features:
            assert np.shape(batch[feature])[0] == batch_size
