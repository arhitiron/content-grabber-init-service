import logging

from flask import Flask
from flask import request

from dto.link_dto import LinkDto


class Server:
    def __init__(self, port, producer):
        self._port = port
        self._app = Flask(__name__)

        @self._app.route("/")
        def main_page():
            return "Simple main page"

        @self._app.route("/start", methods=['POST'])
        def start_from_url():
            logging.log(logging.INFO, request.form)
            url = request.form.get('url')
            link_dto = LinkDto(url)
            producer.add_message(link_dto)
            return link_dto.link + " added to link queue"

    def start(self):
        self._app.run(host='0.0.0.0', port=self._port, debug=True)
