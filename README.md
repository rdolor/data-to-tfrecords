[![Actions Status](https://github.com/rdolor/data_toTFrecords/workflows/Python%20application/badge.svg)](https://github.com/rdolor/data_toTFrecords/actions?query=workflow%3ABuild+branch%3Amaster)

# data_toTFrecords

A simple project to transform a text file to TFRecords.
The standardized format of [iPinYou RTB dataset](https://github.com/wnzhang/make-ipinyou-data) is used.

To install the virtualenv, run `pipenv install --ignore-pipfile`

To convert the text file to TFrecord file, run `python -m data_to_tfrecords.main`

To run the code's tests, do `pytest data_to_tfrecords/test/test_utils.py`
