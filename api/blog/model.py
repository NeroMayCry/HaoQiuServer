# -*- coding: utf-8 -*-
from sqlalchemy import Integer, Sequence, String, ForeignKey

from api import db


class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(Integer, Sequence('blog_id_seq'), primary_key=True)
    username = db.Column(String(64))
    title = db.Column(String(64))
    text = db.Column(String)
    create_time = db.Column(Integer)
