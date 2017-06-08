#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from werkzeug.security import (generate_password_hash, check_password_hash)

from extensions import db
from app.models.base import BaseModel


class Account(BaseModel, db.Model):
    __tablename__ = 'accounts'

    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), unique=True)
    password_hash = db.Column(db.String(256))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
