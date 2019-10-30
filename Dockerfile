FROM  python:3.6-slim-stretch as data-to-tfrecords-base
WORKDIR "/"
RUN apt-get update -qq && \
    apt-get install -yqq --no-install-recommends vim &&  \
    apt-get install -yqq gcc gnupg cron && \
    apt update && \
    apt install -yqq build-essential && \ 
    #Clean-up
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean
RUN pip install --upgrade pip
RUN pip install pipenv
ADD Pipfile.lock . 
ADD Pipfile . 
RUN pipenv install --system --deploy --ignore-pipfile
ADD . .