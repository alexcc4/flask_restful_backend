#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from tests.base import BaseTestCase

from extensions import db
from app.models import Foo


class TestModelFoo(BaseTestCase):
    def test_insert_success(self):
        db.session.add(Foo(name='test'))
        db.session.commit()

        obj = Foo.query.first()
        self.assertIsNotNone(obj)
