# -*- coding: utf-8 -*-
from flask import request, jsonify
from flask.ext.appbuilder._compat import as_unicode

from api import app, db
from api.blog.model import Blog
from api.common import api_resp


@app.route('/blogsubmit', methods=['POST'])
def blog_submit():
    username = request.json.get('username')
    title = request.json.get('title')
    text = request.json.get('text')
    create_time = request.json.get('create_time')

    blog = Blog()

    blog.username = username
    blog.title = title
    blog.text = text
    blog.create_time = create_time

    try:
        db.session.add(blog)
        db.session.commit()
    except Exception as e:
        print as_unicode(e.message)
        db.session.rollback()

    return api_resp.resp('00', None)


@app.route('/blogquery', methods=['POST'])
def blog_query():
    username = request.json.get('username')

    db_blog = db.session.query(Blog).filter(Blog.username == username).all()
    print db_blog
    lst = []
    for blog in db_blog:
        dic = {}
        dic['username'] = blog.username
        dic['title'] = blog.title
        dic['text'] = blog.text
        dic['create_time'] = blog.create_time
        lst.append(dic)

    return api_resp.resp('00', lst)
