#!/bin/sh
BASE=$(dirname $0)
cd $BASE/

TAG="data-to-tfrecords:master"
docker build -t=$TAG ./

