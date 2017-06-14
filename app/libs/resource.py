#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from functools import wraps

from flask_restful import (abort, Resource)
from flask import request
from flask_jwt_extended.view_decorators import (_decode_jwt_from_headers,
                                                check_if_token_revoked)

from extensions import db
from app.models import Account
from app.libs.error import error


class BaseResource(Resource):
    record = None

    @classmethod
    def check_record(cls, model):
        def decorate(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                if len(list(kwargs.keys())) < 2:
                    record_id = list(kwargs.values())[0]
                    record = db.session.query(model).get(record_id)
                    if record is None:
                        abort(404, message='record with id {} not exists.'.format(
                            record_id))

                    cls.record = record
                return func(*args, **kwargs)

            return wrapper

        return decorate

    @classmethod
    def paginate(cls, data, per_page=10, total=0):
        return data, 200, {
            'X-Per-Page': per_page,
            'X-Total': total
        }

    @property
    def current_user(self):
        if not request.headers.get('Authorization'):
            return False

        token = _decode_jwt_from_headers()
        try:
            check_if_token_revoked(token)
        except Exception:
            abort(401, message='token has been revoked.')

        identity = token.get('identity')
        account = Account.query.filter(Account.email == identity).first()

        if account:
            return account

        abort(401, message='token for  {} invalid.'.format(identity))