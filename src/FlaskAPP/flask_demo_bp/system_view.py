#! /usr/bin/env python3.4
# -*- coding: utf-8

from flask.views import MethodView
from flask import render_template, current_app

from FlaskAPP.tasks.demo_task import log
from FlaskAPP.configs import es_api, db
from FlaskAPP.models.blog_model import BlogModel

from . import instance


@instance.before_app_first_request
def modify_auto_escape():
    current_app.jinja_env.autoescape = lambda filename: False


# 首页
class IndexView(MethodView):

    def get(self):
        return 'index.html'


class SearchView(MethodView):

    def get(self, search=None, page=1):
        if search is None:
            ret = {
                'blog_list': [],
                'total': 0,
                'search': '',
            }
            return render_template('search.html', **ret)

        limit = 20
        page = int(page)
        payload = {
            'title': search,
            'limit': limit,
            'offset': (page-1)*limit,
        }
        ret = es_api.query_blog(**payload)
        ret['search'] = search
        return render_template('search.html', **ret)

urls = {
    '/': (IndexView, ['GET', ]),  # 主页
    '/search/<search>/<page>': (SearchView, ['GET', ]), # 搜索
    '/search': (SearchView, ['GET', ]), # 搜索
    '/search/<search>': (SearchView, ['GET', ]), # 搜索
}


for url, items in urls.items():
    if url != '/':
        instance.add_url_rule(
            url,
            view_func=items[0].as_view(url[1:]),
            methods=items[1],
        )
    else:
        instance.add_url_rule(
            '/',
            view_func=IndexView.as_view('index'),
            methods=items[1],
        )
