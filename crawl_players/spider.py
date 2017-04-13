# -*- coding: utf-8 -*-
import math
from bs4 import BeautifulSoup

from api import db
from crawl_players.html_downloader import HtmlDownloader
from crawl_players.html_parser import HtmlParser
from crawl_players.models import PlayerUrl, Player


class Spider(object):
    def __init__(self):
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()

    def start_crawl_players(self):
        offset = 0
        count_in_player_url = db.session.query(PlayerUrl).count()
        print count_in_player_url
        offset = math.floor(count_in_player_url / 100) * 100
        offset = int(offset)
        print offset
        base_url = 'http://sofifa.com/players?offset='
        while offset <= 17600:
            url = base_url + str(offset)
            print url
            html_cont = self.downloader.download_html(url)
            # print html_cont
            soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
            self.parser.get_urls(soup)
            query = db.session.query(PlayerUrl).filter_by(status=False).order_by(PlayerUrl.id.asc()).all()
            for obj in query:
                player = Player()
                player_cont = self.downloader.download_html(obj.url)
                # print player_cont
                soup1 = BeautifulSoup(player_cont, 'html.parser', from_encoding='utf-8')

                meta = soup1.select('.meta')[0].find('span').get_text('|')
                print obj.name
                print meta
                print obj.avatar_url

            offset += 100
            print offset


if __name__ == '__main__':
    spider = Spider()
    spider.start_crawl_players()
