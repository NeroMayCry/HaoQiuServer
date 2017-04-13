# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

log = logging.getLogger(__name__)

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'hahaha'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost/myapp'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

print db.session

import importlib
import os

basepath = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(basepath, '')
modules = []
for dir in os.listdir(path):
    if os.path.isdir(path + '/' + dir):
        modules.append(dir)

modules.sort()

for m in modules:
    try:
        im = importlib.import_module('api.%s.views' % m)
    except Exception as e:
        log.error("{0} error: {1}".format(m, str(e)))

from api.login import views
from api.blog import views
