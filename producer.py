import threading
from collections import deque

from kafka import KafkaProducer


class Producer(threading.Thread):
    daemon = True

    def __init__(self, server, topic):
        super(Producer, self).__init__()
        self._kafka_server = server
        self._kafka_topic = topic
        self._producer = KafkaProducer(bootstrap_servers=server)
        self._messages = deque([])

        self.run()

    def add_message(self, message):
        self._messages.appendleft(message)

    def run(self):
        while True:
            if self._messages:
                self._producer.send(self._kafka_topic, self._messages.pop())
