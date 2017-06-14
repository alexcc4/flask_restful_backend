#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
import http

from tests.base import BaseTestCase
from tests.fixtures.base import AccountFactory


class TestViewLogin(BaseTestCase):
    def test_login_success(self):
        account = AccountFactory.create(password='password')
        response = self.client.post('/api/v1/login', data=json.dumps({
            'email': account.email, 'password': 'password'
        }), headers={'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, http.HTTPStatus.CREATED.value)
        self.assertIn('access_token', response.json)
        self.assertIn('refresh_token', response.json)
