[![Actions Status](https://github.com/rdolor/data_toTFrecords/workflows/Python%20application/badge.svg)](https://github.com/rdolor/data-to-tfrecords/actions)

# Transform txt file data to TFrecords

## Overview
This is a simple module that demonstrates how to transform text file data to TFRecords format.
The project contains:
```
$ tree
.
├── build.sh
├── docker
│   └── Dockerfile
├── ini
│   └── setting.ini
├── output
│   └── train_data_2020-04-10T15:32:34.572126.tf
├── Pipfile
├── Pipfile.lock
├── README.md
├── src
│   ├── config.py
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   └── validate.py
└── tests
    ├── data
    │   ├── TF
    │   │   └── data_to_test.tf
    │   └── TXT
    │       └── test.log.txt
    ├── __init__.py
    └── test_utils.py
```

## Dataset
The text files from the standardized data format of [iPinYou RTB dataset](https://github.com/wnzhang/make-ipinyou-data) is an example of real-life text file datasets that we may want to transform to TFRecords and feed to a TF dataset-based data pipelining when training a model. For testing the code, one of those text files can be moved to `tests/data/TXT` to run the `src/main.py`. This project was tested using the files from campaign 1458.

## How to create the environment

**1. Using pipenv**

* To create or activate a virtual env: `pipenv shell`

    * Install all required packages:
        * install packages exactly as specified in **Pipfile.lock**: `pipenv sync`
        * install using the **Pipfile**, including the dev packages: `pipenv install --dev`

* To run the tests: `pytest`
* To convert a text file to TFrecord file, run: `python -m src.main`

**2. Using docker**

* Build the image: `make build`
* Create a container: `docker run -it data-to-tfrecords:master bash`
* Inside the container, run the main file: `python -m src.main`

