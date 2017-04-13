# -*- coding: utf-8 -*-

from sqlalchemy import Integer, Sequence, String

from api import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = db.Column(String(64))
    password = db.Column(String(256))
    email = db.Column(String(256))
    phone = db.Column(String(256))
    gender = db.Column(String(256))
    id_card = db.Column(String(256))
    birthday = db.Column(String(256))
