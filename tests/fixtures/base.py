#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import factory
from faker import Factory

from app import models
from extensions import db


fake = Factory.create('zh_CN')


class AccountFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = models.Account
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = 'commit'

    id = factory.Sequence(lambda n: n)
    name = factory.Faker('name', locale='zh_CN')
    email = factory.Faker('email')
    password = factory.Faker('pystr')
