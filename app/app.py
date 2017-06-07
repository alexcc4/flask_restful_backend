#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os

import dotenv
from flask import Flask

from app.views import BLUEPRINTS
from extensions import (db, migrate)


# Load dotenv
dotenv_path = os.path.join(
    os.path.dirname(__file__),
    '../.env.' + os.getenv('PYTHON_ENV', 'development')
)
dotenv.load_dotenv(dotenv_path)


class Config(object):
    DEBUG = bool(int(os.getenv('DEBUG')))
    ERROR_404_HELP = bool(int(os.getenv('ERROR_404_HELP')))

    # sqlalchemy setting
    SQLALCHEMY_ECHO = bool(int(os.getenv('SQLALCHEMY_ECHO', 0)))
    SQLALCHEMY_TRACK_MODIFICATIONS = bool(
        int(os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 0)))
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


def create_app(app_name='app', blueprints=None):
    app = Flask(app_name)
    app.config.from_object(Config())

    if blueprints is None:
        blueprints = BLUEPRINTS
    blueprints_resister(app, blueprints)
    extensions_load(app)

    return app


def blueprints_resister(app, blueprints):
    for bp in blueprints:
        app.register_blueprint(bp)


def extensions_load(app):
    db.init_app(app)
    migrate.init_app(app, db)
