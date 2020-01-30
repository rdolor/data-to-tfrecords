[![Actions Status](https://img.shields.io/github/workflow/status/apache/arrow/Python?color=orange&label=actions&logo=github&logoColor=orange&style=for-the-badge)](https://github.com/rdolor/data_toTFrecords/actions)

# data_toTFrecords

A simple project to transform a text file to TFRecords.
The standardized format of [iPinYou RTB dataset](https://github.com/wnzhang/make-ipinyou-data) is used.

To install the virtualenv, run `pipenv install --ignore-pipfile`

To convert the text file to TFrecord file, run `python -m data_to_tfrecords.main`

To run the code's tests, do `pytest data_to_tfrecords/test/test_utils.py`
