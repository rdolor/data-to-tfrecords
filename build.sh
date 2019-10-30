#!/bin/sh
BASE=$(dirname $0)
cd $BASE/

TAG="data_to_tfrecords:dev"
docker build -t=$TAG ./

