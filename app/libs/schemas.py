#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from marshmallow import (Schema, fields, post_dump)
from webargs import fields as fs


page_args = {
    'page': fs.Int(missing=1, validate=lambda val: val > 0),
    'per_page': fs.Int(missing=10, validate=lambda val: val > 0)
}


class BaseSchema(Schema):
    SKIP_VALUES = {None, }

    @post_dump
    def remove_skip_values(self, data):
        return {
            key: value for key, value in data.items()
            if value not in self.SKIP_VALUES
        }


class AccountSchema(BaseSchema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(load_only=True, required=True)
    created_at = fields.DateTime()

    class Meta:
        strict = True


class LoginSchema(BaseSchema):
    email = fields.Email(required=True)
    password = fields.Str(load_only=True, required=True)

    class Meta:
        strict = True


class LogoutSchema(BaseSchema):
    refresh_token = fields.Str(required=True)

    class Meta:
        strict = True


account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)
login_schema = LoginSchema()
logout_schema = LogoutSchema()
