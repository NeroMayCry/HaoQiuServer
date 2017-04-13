# -*- coding: utf-8 -*-
from datetime import datetime

import time

import schedule
from bs4 import BeautifulSoup
from flask.ext.appbuilder._compat import as_unicode

from api import db
from crawl_news.html_downloader import HtmlDownloader
from crawl_news.html_parser import HtmlParser
from crawl_news.models import CrawledUrls, News


class Spider(object):
    def __init__(self):
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()

    def start_crawl(self, root_url):
        root_cont = self.downloader.download(root_url)
        soup = BeautifulSoup(root_cont, 'html.parser', from_encoding='utf-8')
        # self.parser.get_new_urls(soup)
        self.parser.get_urls(soup)

        query_in_news = db.session.query(News).order_by(News.time.desc()).first()

        if query_in_news == None:
            time1 = datetime.min
        else:
            time1 = query_in_news.time

        print time1

        query_in_crawled_urls = db.session.query(CrawledUrls).filter(CrawledUrls.time > time1).order_by(
            CrawledUrls.time.desc()).all()

        for url_obj in query_in_crawled_urls:
            print url_obj.time
            print url_obj.url
            html_cont = self.downloader.download(url_obj.url)
            resp_data = self.parser.parse(url_obj.url, html_cont)
            # print resp_data
            if resp_data.has_key('title'):
                news = News()
                news.title = resp_data['title']
                news.time = resp_data['time']
                news.source = resp_data['source']
                news.content = resp_data['content']
                news.url = resp_data['url']
                news.img_url = resp_data['image_url']
                try:
                    db.session.add(news)
                    db.session.commit()
                except Exception as e:
                    print as_unicode(e.message)
                    db.session.rollback()
            else:
                print '网页格式不合规'


def run_spider(spider, root_url):
    spider.start_crawl(root_url)


if __name__ == '__main__':
    root_url = 'http://news.zhibo8.cc/zuqiu/more.htm'
    spider = Spider()
    run_spider(spider, root_url)
    schedule.every(15).minutes.do(run_spider, spider, root_url)
    while True:
        schedule.run_pending()
        time.sleep(1)
