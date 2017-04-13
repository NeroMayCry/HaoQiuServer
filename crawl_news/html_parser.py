# -*- coding: utf-8 -*-
import re

from bs4 import BeautifulSoup
from flask.ext.appbuilder._compat import as_unicode

from api import db
from crawl_news.models import CrawledUrls


class HtmlParser(object):
    def get_new_urls(self, soup):
        pattern = r"([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8])))"
        links = soup.find_all('a', href=re.compile(pattern=pattern))

        for link in links:
            crawled_urls = CrawledUrls()
            new_url = link['href']
            new_url = 'http:' + new_url
            crawled_urls.url = new_url
            crawled_urls.status = 0
            try:
                db.session.add(crawled_urls)
                db.session.commit()
            except Exception as e:
                print as_unicode(e.message)
                db.session.rollback()

    def get_urls(self, soup):
        print 'get urls'
        lst = soup.select('.articleList')
        # print lst
        for item in lst:
            links = item.find_all('li')
            # print links
            for link in links:
                crawled_urls = CrawledUrls()
                hrf = link.find('a').get('href')
                hrf = 'http:' + hrf
                time = link.select('.postTime')[0].get_text()
                query = db.session.query(CrawledUrls).filter_by(url=hrf).first()
                if query:
                    print 'this url has been crawled'
                else:
                    print hrf
                    print time
                    crawled_urls.url = hrf
                    crawled_urls.time = time
                    try:
                        db.session.add(crawled_urls)
                        db.session.commit()
                    except Exception as e:
                        print as_unicode(e.message)
                        db.session.rollback()

        # links = soup.select('.dataList')
        # print links
        # for link in links:
        #     crawled_urls = CrawledUrls()
        #     hrf = link.find('a').get('href')
        #     hrf = 'http:' + hrf
        #     time = link.select('.postTime')[0].get_text()
        #     query = db.session.query(CrawledUrls).filter_by(url=hrf).first()
        #     if query:
        #         print 'this url has been crawled'
        #     else:
        #         print hrf
        #         print time
        #         crawled_urls.url = hrf
        #         crawled_urls.time = time
        #         try:
        #             db.session.add(crawled_urls)
        #             db.session.commit()
        #         except Exception as e:
        #             print as_unicode(e.message)
        #             db.session.rollback()



    def parse(self, url, html_cont):
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        resp_data = {}
        resp_data['url'] = url
        try:
            title = soup.select('.title')[0].find('h1').string
            text = soup.select('.title')[0].find('span').get_text(',')
            content = soup.select('.content')[0].get_text()
            image = soup.select('.content')[0].find('img').get('src')
            strlst = text.split(',')

            resp_data['title'] = title
            resp_data['time'] = strlst[0]
            resp_data['source'] = strlst[1]
            resp_data['content'] = content
            resp_data['image_url'] = image

        except:
            print 'list page'
        # print resp_data
        return resp_data

