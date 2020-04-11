import os

SECRET_KEY = os.environ.get('AM_I_IN_A_DOCKER_CONTAINER', False)
kafka_broker = 'error in broker_detection'
cassandra_cluster = 'error in broker_detection'

if SECRET_KEY:
    print('I am running in a Docker container')
    kafka_broker = 'kafka://kafka:9093'
    cassandra_cluster = 'cassandra'
else:
    print('I am running on local enterpreter')
    kafka_broker = 'kafka://localhost:9092'
    cassandra_cluster = 'localhost'
