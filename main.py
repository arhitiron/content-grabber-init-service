import logging
import os

from producer import Producer
from server import Server

INIT_PORT = int(os.environ['INIT_PORT'])
KAFKA_ADDR = os.environ['KAFKA_ADDRESS']
LINK_QUEUE_TOPIC = os.environ['LINK_QUEUE_TOPIC']


class InitService(object):
    # TODO: add default values
    def __init__(self, port, kafka_addr, link_queue_topic):
        producer = Producer(kafka_addr, link_queue_topic)

        self._server = Server(port, producer)
        producer.start()

    def serve(self):
        self._server.start()


def main():
    service = InitService(INIT_PORT, KAFKA_ADDR, LINK_QUEUE_TOPIC)
    service.serve()


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()
