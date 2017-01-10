import json
import sys
import threading
import time
from collections import deque

from kafka import KafkaProducer


class Producer(threading.Thread):
    daemon = True

    def __init__(self, server, topic):
        super(Producer, self).__init__()
        self._kafka_server = server
        self._kafka_topic = topic
        self._messages = deque()
        self._lock = threading.Lock()

    def add_message(self, message):
        self._lock.acquire()
        self._messages.appendleft(message)
        self._lock.release()

    def producer_optimistic_init(self):
        try:
            producer = KafkaProducer(bootstrap_servers=self._kafka_server,
                                     value_serializer=lambda v: json.dumps(v,
                                                                           default=convert_to_builtin_type).encode(
                                         'utf-8'))
            return producer
        except:
            time.sleep(1)
            print "Unexpected error:", sys.exc_info()[0]
            return self.producer_optimistic_init()

    def run(self):
        producer = self.producer_optimistic_init()
        while True:
            if self._messages:
                msg = self._messages.pop()
                producer.send(self._kafka_topic, msg)


def convert_to_builtin_type(obj):
    d = {}
    d.update(obj.__dict__)
    return d
