
# -*- coding:utf-8 -*- 
# time: 2020/3/7--19:49
__author__ = 'Henry'

from Movie.app import app
from Movie.app import db
from flask_script import Manager # type: ignore
from flask_migrate import Migrate, MigrateCommand # type: ignore

manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()

    #app.run()
    #app.run(port=8080)
