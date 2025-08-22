import logging
import sys
import os
from logging import log
from flask import Flask
from src.app_flask_archetype.api.api import app_api
from src.app_flask_archetype.api.health_check import health_check_api

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def create_app(test_config=None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(app_api, url_prefix="/app_flask_archetype/api")
    app.register_blueprint(health_check_api, url_prefix="/app_flask_archetype/api")

    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app


if __name__ == "__main__":
    log(logging.INFO, "Starting up app_flask_archetype")
    create_app().run()
