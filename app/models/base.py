#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import datetime

from extensions import db


class BaseModel(object):
    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow,
                           onupdate=datetime.datetime.utcnow)
