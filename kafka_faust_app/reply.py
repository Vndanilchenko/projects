import faust
from time import sleep
from service import getResponseForText
import random
from multiprocessing import Pool
from broker_detection import kafka_broker

class Message(faust.Record):
    name: str

app = faust.App(
    'greetings_group',
    broker=kafka_broker,
    autodiscover=True,
    topic_partitions=7)


response_topic = app.topic('response_topic', value_type=Message, partitions=7)

@app.agent(response_topic)
async def reply(stream):
    async for message in stream:
        print('response', getResponseForText(message.name))
