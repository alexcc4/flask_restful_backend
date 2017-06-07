#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from flask_script import Manager
from flask_migrate import MigrateCommand

from app.app import create_app
from app import models


manager = Manager(create_app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
