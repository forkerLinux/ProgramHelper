#!/usr/bin/env python3
# coding:utf-8

import requests
from urllib.parse import urljoin

from FlaskAPP.utils.log_util import init_log


class EsApi(object):
    base_url = None

    def init_app(self, app):
        self.base_url = app.config.get('ES_URL')
        self.logger = init_log(debug=app.config.get('DEBUG', True))

    def query_blog(self, **kwargs):
        blog_list = []
        total = 0
        try:
            url = urljoin(self.base_url, 'blog')
            r = requests.post(url, json=kwargs)
            blog_list = r.json()['blog_list']
            total = r.json()['total']
        except Exception as e:
            self.logger.exception(e)

        ret = {
            'blog_list': blog_list,
            'total': total,
        }
        return ret
