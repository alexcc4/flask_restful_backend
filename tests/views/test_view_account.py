#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
import http

from tests.base import BaseTestCase
from tests.fixtures.base import AccountFactory

from app.libs.schemas import account_schema
from app.models import Account


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
        data['password'] = 'random'
        response = self.client.post(
            '/api/v1/accounts',
            data=json.dumps(al.data),
            headers={'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, http.HTTPStatus.CREATED.value)

    def test_account_get_success(self):
        account = AccountFactory.create()
        response = self.client.get('/api/v1/accounts/{}'.format(account.id))

        self.assert200(response)
        self.assertIn('id', response.json)
        self.assertIn('email', response.json)

    def test_account_delete_success(self):
        account = AccountFactory.create()
        response = self.client.delete('/api/v1/accounts/{}'.format(account.id))

        self.assertEqual(response.status_code, 204)
        al = Account.query.get(account.id)
        self.assertIsNone(al)

    def test_account_update_success(self):
        account = AccountFactory.create()

        account_new = AccountFactory.build()
        al = account_schema.dump(account_new)
        data = al.data
        data.pop('id')
        data['password'] = 'random'

        response = self.client.put(
            '/api/v1/accounts/{}'.format(account.id),
            data=json.dumps(data),
            headers={'Content-Type': 'application/json'})

        self.assert200(response)
        self.assertEqual(response.json['name'], data['name'])
