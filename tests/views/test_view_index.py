#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from tests.base import BaseTestCase


class TestViewIndex(BaseTestCase):
    def test_index(self):
        response = self.client.get('/api/v1/index')

        self.assert200(response)
