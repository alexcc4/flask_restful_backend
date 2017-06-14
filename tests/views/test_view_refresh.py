#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
import http

from flask_jwt_extended import create_refresh_token

from tests.base import BaseTestCase
from tests.fixtures.base import AccountFactory


class TestViewRefresh(BaseTestCase):
    def test_login_success(self):
        account = AccountFactory.create()
        refresh_token = create_refresh_token(account.email)

        response = self.client.post(
            '/api/v1/refresh', data=json.dumps({}),
            headers={'Content-Type': 'application/json',
                     'Authorization': 'Bearer ' + refresh_token})

        self.assertEqual(response.status_code, http.HTTPStatus.CREATED.value)
        self.assertIn('access_token', response.json)
