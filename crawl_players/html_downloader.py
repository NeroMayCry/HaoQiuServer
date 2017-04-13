# -*- coding: utf-8 -*-
import requests


class HtmlDownloader(object):
    def download_html(self, url):
        if url is None:
            print 'url is None'
            return None

        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}

        html = requests.get(url, headers=header)

        html.encoding = 'utf-8'  # 这一行是将编码转为utf-8否则中文会显示乱码。
        # print html.text

        return html.text
