#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from flask import (Blueprint, request)
from flask_restful import (Resource, Api)

from app.models import Account
from extensions import db
from app.libs.schemas import (account_schema, accounts_schema)
from app.libs.decorators import BaseResource


class AccountsResource(Resource):
    def get(self):
        result = accounts_schema.dump(
            Account.query.order_by(Account.id.desc()).all())

        return result.data

    def post(self):
        json_data = request.json
        data, errors = account_schema.load(json_data)
        if errors:
            return {
                       'errors': errors, 'errcode': 422, 'message': '创建新用户失败'
                   }, 422

        account = Account(**data)
        db.session.add(account)
        try:
            db.session.commit()
        except Exception as e:
            return {
                       'errors': str(e), 'errcode': 422, 'message': '创建新用户失败'
                   }, 422

        result = account_schema.dump(account)
        return result.data, 201


class AccountResource(BaseResource):
    @BaseResource.check_record(Account)
    def get(self, account_id):
        result = account_schema.dump(self.record)
        return result.data

    @BaseResource.check_record(Account)
    def put(self, account_id):
        json_data = request.json
        data, errors = account_schema.load(json_data)
        if errors:
            return {
                       'errors': errors, 'errcode': 422, 'message': '创建新用户失败'
                   }, 422

        for k, v in data.items():
            setattr(self.record, k, v)
        db.session.add(self.record)
        try:
            db.session.commit()
        except Exception as e:
            return {
                       'errors': str(e), 'errcode': 422, 'message': '更新用户失败'
                   }, 422
        result = account_schema.dump(self.record)
        return result.data

    @BaseResource.check_record(Account)
    def delete(self, account_id):
        db.session.delete(self.record)
        db.session.commit()
        return None, 204


account_bp = Blueprint('account', __name__)
account_api = Api(account_bp, prefix='/api/v1')
account_api.add_resource(AccountsResource, '/accounts')
account_api.add_resource(AccountResource, '/accounts/<int:account_id>')
