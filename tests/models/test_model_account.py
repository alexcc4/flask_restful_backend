#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from tests.base import BaseTestCase

from extensions import db
from app.models import Account
from tests.fixtures.base import AccountFactory


class TestModelAccount(BaseTestCase):
    def test_insert_success(self):
        account = AccountFactory.build()
        db.session.add(account)
        db.session.commit()

        obj = Account.query.first()
        self.assertIsNotNone(obj)
