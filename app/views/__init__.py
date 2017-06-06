#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from app.views.index import index_bp


BLUEPRINTS = (index_bp,)
__all__ = ['BLUEPRINTS']

