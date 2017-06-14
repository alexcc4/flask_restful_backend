#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json

from flask_jwt_extended import (create_refresh_token, create_access_token)

from tests.base import BaseTestCase
from tests.fixtures.base import AccountFactory


class TestViewLogout(BaseTestCase):
    def test_login_success(self):
        account = AccountFactory.create()

        access_token = create_access_token(account.email)
        refresh_token = create_refresh_token(account.email)

        response = self.client.post('/api/v1/logout', data=json.dumps({
            'refresh_token': refresh_token }), headers={
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + access_token})

        self.assert200(response)
