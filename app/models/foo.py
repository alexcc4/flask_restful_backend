#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from extensions import db
from app.models.base import BaseModel


class Foo(BaseModel, db.Model):
    __tablename__ = 'foos'

    name = db.Column(db.String(256), nullable=False)
    gender = db.Column(db.String(128))
