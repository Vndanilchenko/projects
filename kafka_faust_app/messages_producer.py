import faust
from preprocess import preprocess
import random
from broker_detection import kafka_broker

app = faust.App(
    'greetings_group',
    broker=kafka_broker,
    autodiscover=True)

@app.timer(2.0)
async def publish_greetings():
    print('sending message')
    random_name = random.choice(['Vadim', 'Lena', 'Sergey', 'Ildar'])
    await preprocess.send(value={"name":random_name})
