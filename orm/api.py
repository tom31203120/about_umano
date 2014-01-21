#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
from functools import partial

from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, TEXT, ENUM
from sqlalchemy import Column

from lib.database import Base, backend, model_to_dict

NotNullColumn = partial(Column, nullable=False, server_default='')

class LabelDetail(Base):

    __tablename__ = 'label_detail'

    id = Column(INTEGER, primary_key=True)
    _id = Column(VARCHAR(32), nullable=False, server_default='')
    image_url = Column(VARCHAR(256), nullable=False, server_default='')
    name = Column(VARCHAR(256), nullable=False, server_default='')
    level = Column(INTEGER, nullable=False, server_default='1')

class ApiModel(object):

    def __init__(self):
        self.master = backend.get_session('common',master=True)
        self.slave = backend.get_session('common')

    def models_to_list(self, models):
        ret = []
        for model in models:
            data = dict((key, getattr(model, key)) for key in model.keys())
            ret.append(data)
        return ret

class LabelModel(ApiModel):

    def get_all(self):
        favlist = []
        favlist = (self.slave.query(LabelDetail._id, LabelDetail.name).all())
        favlist = self.models_to_list(favlist)
        return favlist

    def add(self, data={}):
        fav = LabelDetail(**data)
        self.master.add(fav)
        self.master.commit()
        return True
