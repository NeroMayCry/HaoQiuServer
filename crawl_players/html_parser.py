# -*- coding: utf-8 -*-
from flask.ext.appbuilder._compat import as_unicode

from api import db
from crawl_players.models import PlayerUrl


class HtmlParser(object):
    def get_urls(self,soup):
        base_url = 'http://sofifa.com'
        trs = soup.tbody.find_all('tr')
        print trs
        for tr in trs:
            player_urls = PlayerUrl()

            td = tr.select('.nowrap')[0]
            hrf = td.find('a').get('href')
            hrf = base_url + hrf
            query = db.session.query(PlayerUrl).filter_by(url=hrf).first()

            if query:
                print 'this player url has been added to our database'
            else:
                player_name = td.find('a').get('title')
                player_id = td.find('img').get('id')
                avatar_url = td.find('img').get('data-src')

                player_urls.url = hrf
                player_urls.name = player_name
                player_urls.player_id = player_id
                player_urls.avatar_url = avatar_url
                player_urls.status = False

                try:
                    db.session.add(player_urls)
                    db.session.commit()
                except Exception as e:
                    print as_unicode(e.message)
                    db.session.rollback()

    # def parse_player_cont(self, soup):






