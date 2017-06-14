#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api
from flask_jwt_extended import (
    create_access_token, jwt_refresh_token_required, get_jwt_identity)

from app.libs.resource import BaseResource


class RefreshResource(BaseResource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        return {
                   'access_token': create_access_token(identity=current_user)
               }, 201


refresh_bp = Blueprint('refresh', __name__)
refresh_api = Api(refresh_bp, prefix='/api/v1')
refresh_api.add_resource(RefreshResource, '/refresh')
