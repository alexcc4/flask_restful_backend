#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api
from webargs.flaskparser import use_args
from flask_jwt_extended import (create_access_token, create_refresh_token)

from app.libs.resource import BaseResource
from app.libs.schemas import (login_schema, account_schema)
from app.libs.error import error
from app.models import Account


class LoginResource(BaseResource):
    @use_args(login_schema)
    def post(self, args):
        account = Account.query.filter(Account.email == args.get('email')).first()
        if account is None:
            return error({}, 400, errors={'email': '邮箱不存在'})

        if not account.verify_password(args.get('password')):
            return error({}, 400, errors={'password': '密码错误'})

        data = account_schema.dump(account).data
        data['access_token'] = create_access_token(identity=args.get('email'))
        data['refresh_token'] = create_refresh_token(identity=args.get('email'))

        return data, 201

login_bp = Blueprint('login', __name__)
login_api = Api(login_bp, prefix='/api/v1')
login_api.add_resource(LoginResource, '/login')
