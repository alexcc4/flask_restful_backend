#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os

from flask_testing import TestCase

from extensions import db


os.environ['PYTHON_ENV'] = 'test'


class BaseTestCase(TestCase):
    def create_app(self):
        from app.app import create_app

        app = create_app(__name__)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
