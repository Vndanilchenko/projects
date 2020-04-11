from time import time
from cassandra_utils import create_connection, increase_and_get_number_of_greetings

def sleep(t):
    """simple sleep function, which loads CPU"""
    start = time()
    s = 0
    while time() - start < t:
        for i in range(100_000):
            s += i

session = create_connection()
def getResponseForText(message):
    sleep(3)
    message = str(message)
    c = increase_and_get_number_of_greetings(session, message)
    return f'hello, {message}! Already seen {c} times'
