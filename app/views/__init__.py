#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from app.views.index import index_bp
from app.views.account import account_bp


BLUEPRINTS = (index_bp, account_bp)
__all__ = ['BLUEPRINTS']

