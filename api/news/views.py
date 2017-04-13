# -*- coding: utf-8 -*-
from flask import request

from api import app, db
from api.common import api_resp
from crawl_news.models import News


@app.route('/newsinban', methods=['GET'])
def news_in_ban():
    page_size = 5
    query = db.session.query(News).order_by(News.time.desc())
    items = query.limit(page_size)
    lst = []
    for item in items:
        dic = {}
        dic['title'] = item.title
        dic['time'] = str(item.time)
        # print item.time
        dic['source'] = item.source
        dic['pic'] = item.img_url
        lst.append(dic)

    return api_resp.resp('00', lst)


@app.route('/getnewslist', methods=['GET'])
def get_news():
    page = request.args.get('page')
    # print page
    page_size = 20
    query = db.session.query(News).order_by(News.time.desc())
    if page:
        page = int(page)
        query = query.offset(page * page_size + 5)

    items = query.limit(page_size)
    # print items
    lst = []
    for item in items:
        dic = {}
        dic['title'] = item.title
        dic['time'] = str(item.time)
        # print item.time
        dic['source'] = item.source
        dic['pic'] = item.img_url
        lst.append(dic)

    return api_resp.resp('00', lst)

@app.route('/getnewsdetail', methods=['POST'])
def get_detail():
    title = request.json.get('title')
    print title

    query = db.session.query(News).filter_by(title=title).first()

    dic = {}
    dic['title'] = query.title
    dic['time'] = str(query.time)
    dic['source'] = query.source
    dic['content'] = query.content
    dic['img_url'] = query.img_url

    return api_resp.resp('00', dic)

