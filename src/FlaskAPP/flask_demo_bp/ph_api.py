#!/usr/bin/env python3.4
# coding:utf-8

from flask.views import MethodView
from flask import render_template, current_app

from . import instance


class BlogView(MethodView):

    def get(self, page):
        pass


urls = {
    '/blog/<page>': (BlogView, ['GET', ]),
}


for url, items in urls.items():
    instance.add_url_rule(
        url,
        view_func=items[0].as_view(url[1:]),
        methods=items[1],
    )
