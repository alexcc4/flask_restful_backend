#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from marshmallow import Schema, fields


class AccountSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(load_only=True, required=True)
    created_at = fields.DateTime()


account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)
