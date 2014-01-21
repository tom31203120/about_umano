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

class UmanoDetail(Base):

    __tablename__ = 'umano_detail'

    id = Column(INTEGER, primary_key=True)
    _id= Column(VARCHAR(32), index=True, nullable=False, server_default='')
    has_05x = Column(INTEGER, nullable=False, server_default='0')
    has_2x  = Column(INTEGER, nullable=False, server_default='0')
    created = Column(VARCHAR(32), nullable=False, server_default='')
    recorded= Column(VARCHAR(32), nullable=False, server_default='')
    description= Column(VARCHAR(256), nullable=False, server_default='')
    download_url= Column(VARCHAR(256), nullable=False, server_default='')
    download_url_2x= Column(VARCHAR(256), nullable=False, server_default='')
    gender= Column(INTEGER, nullable=False, server_default='0')
    guid= Column(INTEGER, nullable=False, server_default='0')
    image_url = Column(VARCHAR(256), nullable=False, server_default='')
    length= Column(INTEGER, nullable=False, server_default='0')
    name= Column(VARCHAR(256), nullable=False, server_default='')
    source_name= Column(VARCHAR(32), nullable=False, server_default='')
    source_id= Column(VARCHAR(32), nullable=False, server_default='')
    source_url= Column(VARCHAR(256), nullable=False, server_default='')
    status = Column(VARCHAR(12), nullable=False, server_default='')
    stream_url= Column(VARCHAR(256), nullable=False, server_default='')
    stream_url_2x= Column(VARCHAR(256), nullable=False, server_default='')
    thumbnail_url= Column(VARCHAR(256), nullable=False, server_default='')

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

class UmanoModel(ApiModel):

    def get_all(self):
        favlist = []
        favlist = (self.slave.query(UmanoDetail._id, UmanoDetail.name).all())
        favlist = self.models_to_list(favlist)
        return favlist

    def select(self, data={}):
        return self.slave.query(UmanoDetail).filter(data['_id']==UmanoDetail._id).first()

    #def delete(self, data={}):
        #open_id  = data['open_id']
        #music_no = data['music_no']
        ##self.master.query(UserFavModel).filter(UserFavModel.music_no==music_no, UserFavModel.open_id==open_id).delete()
        #self.master.commit()
        #return True

    def add(self, data={}):
        if not self.select(data):
            fav = UmanoDetail(**data)
            self.master.add(fav)
            self.master.commit()
        return True
