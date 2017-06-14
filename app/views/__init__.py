#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from app.views.index import index_bp
from app.views.account import account_bp
from app.views.auth.login import login_bp
from app.views.auth.refresh import refresh_bp
from app.views.auth.logout import logout_bp


BLUEPRINTS = (index_bp, account_bp, login_bp, refresh_bp, logout_bp,)
__all__ = ['BLUEPRINTS']

