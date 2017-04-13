# -*- coding: utf-8 -*-
from sqlalchemy import Integer, Sequence, String, DateTime

from api import db


class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(Integer, Sequence('football_news_id_seq'), primary_key=True)
    title = db.Column(String(64))
    time = db.Column(DateTime)
    source = db.Column(String(64))
    content = db.Column(String)
    url = db.Column(String)
    img_url = db.Column(String)


class CrawledUrls(db.Model):
    __tablename__ = 'crawled_urls'

    id = db.Column(Integer, Sequence('crawl_url_id_seq'), primary_key=True)
    url = db.Column(String)
    time = db.Column(DateTime)
    # status = db.Column(Integer)
