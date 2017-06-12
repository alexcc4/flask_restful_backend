#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from webargs.flaskparser import (parser, abort)


@parser.error_handler
def handler_request_parsing_error(e):
    error({}, 400, errors=e.messages)


def error(params=None, code=422, message='不合法的请求', errors=None):
    params['message'] = message
    params['errcode'] = code
    if errors:
        params['errors'] = errors

    abort(code, **params)
