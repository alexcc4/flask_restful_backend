#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
import http

from tests.base import BaseTestCase
from tests.fixtures.base import AccountFactory

from app.libs.schemas import account_schema


class TestViewIndex(BaseTestCase):
    def test_accounts_list(self):
        for _ in range(3):
            AccountFactory.create()
        response = self.client.get('/api/v1/accounts')

        self.assert200(response)
        self.assertEqual(len(response.json), 3)

    def test_account_create_success(self):
        account = AccountFactory.build()
        al = account_schema.dump(account)
        data = al.data
        data.pop('created_at')
        data['password'] = 'random'
        response = self.client.post(
            '/api/v1/accounts',
            data=json.dumps(al.data),
            headers={'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, http.HTTPStatus.CREATED.value)
