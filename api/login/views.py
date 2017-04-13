# -*- coding: utf-8 -*-
from flask import request
from flask.ext.appbuilder._compat import as_unicode

from api import db
from api.common import api_resp
from api.login.model import User
from run import app


@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')

    db_user = db.session.query(User).filter_by(username=username).order_by('id asc').first()
    if db_user:
        return api_resp.resp('01', None)

    db_user_email = db.session.query(User).filter_by(email=email).order_by('id asc').first()
    if db_user_email:
        return api_resp.resp('02', None)

    user = User()
    user.username = username
    user.password = password
    user.email = email

    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        print as_unicode(e.message)
        db.session.rollback()

    return api_resp.resp('00', None)


@app.route('/login', methods=['POST'])
def login():
    print request.json

    username = request.json.get('username')
    password = request.json.get('password')

    db_user = db.session.query(User).filter_by(username=username).first()
    if not db_user:
        return api_resp.resp('03', None)

    if password != db_user.password:
        return api_resp.resp('04', None)

    return api_resp.resp('00', None)
