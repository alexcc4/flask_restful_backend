#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from flask import (Blueprint, request)
from flask_restful import (Api, abort)
from webargs.flaskparser import (use_args, parser)
from flask_jwt_extended import jwt_required

from app.models import Account
from extensions import db
from app.libs.schemas import (account_schema, accounts_schema, page_args)
from app.libs.resource import BaseResource
from app.libs.error import error


class AccountsResource(BaseResource):
    @jwt_required
    @use_args(page_args, locations=('query',))
    def get(self, args):
        accounts = Account.query.order_by(Account.id.desc()).paginate(
            args.get('page'), args.get('per_page'))
        result = accounts_schema.dump(accounts.items)

        return self.paginate(result.data, accounts.per_page, accounts.total)

    # @jwt_required
    @use_args(account_schema)
    def post(self, args):
        account = Account(**args)
        db.session.add(account)
        try:
            db.session.commit()
        except Exception as e:
            return error({}, 422, errors={'email': [str(e)]})

        result = account_schema.dump(account)
        return result.data, 201


class AccountResource(BaseResource):
    @jwt_required
    @BaseResource.check_record(Account)
    def get(self, account_id):
        result = account_schema.dump(self.record)
        return result.data

    @jwt_required
    @BaseResource.check_record(Account)
    def put(self, account_id):
        args = parser.parse(account_schema, request)
        for k, v in args.items():
            setattr(self.record, k, v)
        db.session.add(self.record)
        try:
            db.session.commit()
        except Exception as e:
            return error({}, 422, errors={'email': [str(e)]})

        result = account_schema.dump(self.record)

        return result.data

    @jwt_required
    @BaseResource.check_record(Account)
    def delete(self, account_id):
        if self.current_user and self.current_user.id == account_id:
            db.session.delete(self.record)
            db.session.commit()
            return None, 204

        return abort(403, message='only can be deleted by himself')

account_bp = Blueprint('account', __name__)
account_api = Api(account_bp, prefix='/api/v1')
account_api.add_resource(AccountsResource, '/accounts')
account_api.add_resource(AccountResource, '/accounts/<int:account_id>')
