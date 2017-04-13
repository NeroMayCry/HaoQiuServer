# -*- coding: utf-8 -*-
from sqlalchemy import Integer, Sequence, String, Boolean

from api import db


class PlayerUrl(db.Model):
    __tablename__ = 'player_url'

    id = db.Column(Integer, Sequence('player_url_id_seq'), primary_key=True)
    url = db.Column(String)
    name = db.Column(String(128))
    player_id = db.Column(String(64))
    avatar_url = db.Column(String)
    status = db.Column(Boolean)

class Player(db.Model):
    __tablename__ = 'player'

    id = db.Column(Integer, Sequence('player_id_seq'), primary_key=True)
    name = db.Column(String(64))
    meta = db.Column(String(256))
    avatar_url = db.Column(String)