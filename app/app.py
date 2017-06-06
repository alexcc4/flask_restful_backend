#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os

import dotenv
from flask import Flask

from app.views import BLUEPRINTS


# Load dotenv
dotenv_path = os.path.join(
    os.path.dirname(__file__),
    '../.env.' + os.getenv('PYTHON_ENV', 'development')
)
dotenv.load_dotenv(dotenv_path)


class Config(object):
    DEBUG = bool(int(os.getenv('DEBUG')))
    ERROR_404_HELP = bool(int(os.getenv('ERROR_404_HELP')))


def create_app(app_name='app', blueprints=None):
    app = Flask(app_name)
    app.config.from_object(Config())

    if blueprints is None:
        blueprints = BLUEPRINTS
    blueprints_resister(app, blueprints)

    return app


def blueprints_resister(app, blueprints):
    for bp in blueprints:
        app.register_blueprint(bp)
