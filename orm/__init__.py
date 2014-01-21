#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
from orm.api import ApiModel, LabelModel, UmanoModel

class ORM(object):

    def __init__(self):
        self.api = ApiModel()
        self.label = LabelModel()
        self.umano = UmanoModel()

# global
orm = ORM()


