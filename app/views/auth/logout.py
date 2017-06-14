#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api
from flask_jwt_extended import (
    jwt_required, get_raw_jwt, revoke_token, unrevoke_token)
from flask_jwt_extended.utils import get_jti
from webargs.flaskparser import use_args

from app.libs.resource import BaseResource
from app.libs.schemas import logout_schema
from app.libs.error import error


class LogoutResource(BaseResource):
    @jwt_required
    @use_args(logout_schema)
    def post(self, args):
        try:
            _revoke_current_token()
        except KeyError:
            return {
                       'error': 'Access token not found in the blacklist store'
                   }, 401

        jti = get_jti(args.get('refresh_token'))
        try:
            revoke_token(jti)
        except Exception as e:
            _unrevoke_current_token()
            return error({}, 422, errors={'refresh_token': [str(e)]})

        return {}, 200


def _revoke_current_token():
    current_token = get_raw_jwt()
    jti = current_token['jti']
    revoke_token(jti)


def _unrevoke_current_token():
    current_token = get_raw_jwt()
    jti = current_token['jti']
    unrevoke_token(jti)


logout_bp = Blueprint('logout', __name__)
logout_api = Api(logout_bp, prefix='/api/v1')
logout_api.add_resource(LogoutResource, '/logout')
