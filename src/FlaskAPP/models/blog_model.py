#! /usr/bin/env python3.4
# -*- coding: utf-8 -*-

from datetime import datetime
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.mysql import LONGTEXT
from FlaskAPP.configs import db, logger


class BlogModel(db.Model):
    __tablename__ = 'blog'

    id = db.Column(db.BIGINT, primary_key=True)
    url = db.Column(db.String(255), unique=True)
    title = db.Column(db.String(255))
    category = db.Column(db.String(255))
    subcategory = db.Column(db.String(255))
    fetch_time = db.Column(db.DateTime)
    create_time = db.Column(db.DateTime)
