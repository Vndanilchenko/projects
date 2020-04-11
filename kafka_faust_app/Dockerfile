FROM python:3.7-slim
MAINTAINER Archit Dwivedi "architdwivedi00@gmail.com"

ENV HOME /root
ENV APP_HOME /application/
ENV C_FORCE_ROOT=true
ENV PYTHONUNBUFFERED 1
ENV WORKER_DATA_DIRECTORY /data/

#RUN apk update
#RUN apk add
#RUN apt-get update -y --fix-missing \
#  && apt-get install -y \
#    build-essential \
#    curl \
#    libgflags-dev \
#    libsnappy-dev \
#    zlib1g-dev \
#    libbz2-dev \
#    liblz4-dev


ENV LD_LIBRARY_PATH=/usr/local/lib \
  PORTABLE=1

#RUN cd /tmp \
#  && curl -sL rocksdb.tar.gz https://github.com/facebook/rocksdb/archive/v5.15.10.tar.gz > rocksdb.tar.gz \
#  && tar fvxz rocksdb.tar.gz \
#  && cd rocksdb-5.15.10 \
#  && make shared_lib \
#  && make install-shared


#RUN apt-get remove -y \
#  build-essential \
#  curl \
#  && rm -rf /tmp


# Install bundle of gems
RUN mkdir -p $APP_HOME
RUN mkdir -p $WORKER_DATA_DIRECTORY
WORKDIR $APP_HOME

# Install pip packages
ADD ./requirements.txt $APP_HOME
#RUN pip install --upgrade pip setuptools wheel
RUN pip install -r $APP_HOME/requirements.txt
#RUN pip install faust
#RUN pip install cassandra-driver
#CMD ["faust", "-A", "test", "worker", "-l", "info"]
#RUN rm $APP_HOME/requirements.txt
