#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
from simplekv.memory.redisstore import RedisStore

from flask_testing import TestCase
import fakeredis

from extensions import db


os.environ['PYTHON_ENV'] = 'test'


class BaseTestCase(TestCase):
    def create_app(self):
        from app.app import create_app

        app = create_app(__name__)
        app.config['TESTING'] = True
        self.r = fakeredis.FakeStrictRedis()
        app.extensions['redis'] = self.r
        app.config['JWT_BLACKLIST_STORE'] = RedisStore(self.r)

        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

        self.r.flushall()
