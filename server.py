from flask import Flask


class Server:
    def __init__(self, addr, producer):
        self._app = Flask(__name__)
        self._app.config['SERVER_NAME'] = addr

        @self._app.route("/")
        def init_service():
            # TODO: hardcoded, change to get param
            producer.add_message("https://www.olx.ua/")

    def start(self):
        self._app.run(debug=True)
