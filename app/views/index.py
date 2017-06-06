#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from flask import Blueprint
from flask_restful import (Resource, Api)


class IndexResource(Resource):
    def get(self):
        return {
            'hello': 'hello world!'
        }


index_bp = Blueprint('index', __name__)
index_api = Api(index_bp, prefix='/api/v1')
index_api.add_resource(IndexResource, '/index')
