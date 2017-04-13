# -*- coding: utf-8 -*-
from api import db
from crawl_players.models import PlayerUrl


class DbTools(object):
    def reset_payer_url_status(self):
        query = db.session.query(PlayerUrl).filter_by(status=True).all()
        if query:
            for obj in query:
                print obj.status
                obj.status = False
                db.session.commit()
        else:
            print 'query is empty'

if __name__ == '__main__':
    db_tools = DbTools()
    db_tools.reset_payer_url_status()
