#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os

from flask_testing import TestCase

from app.app import create_app


os.environ['PYTHON_ENV'] = 'test'


class BaseTestCase(TestCase):
    def create_app(self):
        app = create_app(__name__)
        app.config['TESTING'] = True

        return app

    def setUp(self):
        pass

    def tearDown(self):
        pass
