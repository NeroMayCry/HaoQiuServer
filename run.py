# -*- coding: utf-8 -*-
import threading

import time

from api import app, db
from crawl_players.models import PlayerUrl
from crawl_players.models import Player

if __name__ == '__main__':
    db.session.remove()
    db.create_all()
    # app.run(host='127.0.0.1', port=8787, debug=True, use_reloader=False)
    app.run(host='192.168.31.120', port=8787, debug=True, use_reloader=False)
    # app.run(host='192.168.31.119', port=8787, debug=True, use_reloader=False)
