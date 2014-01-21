#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:

import random
from functools import partial

from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import class_mapper

from consts import MYSQL

class Model(object):

    @declared_attr
    def __tablename__(cls):
        name = cls.__name__
        return name

    @declared_attr
    def __table_args__(cls):
        return {
            'mysql_engine': 'InnoDB',
            'mysql_charset': 'utf8'
        }

    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

Base = declarative_base(cls=Model)

def create_session(engine):
    if not engine:
        return None
    session = scoped_session(sessionmaker(bind=engine))
    return session()


class Backend(object):

    def __init__(self, debug):
        master = MYSQL['master']
        slaves = MYSQL['slaves']
        dbs = MYSQL['dbs']
        schema = 'mysql://%s:%s@%s:%d/%s?charset=utf8'
        kwargs = {
            'pool_recycle': 3600,
            'echo': debug,
            'echo_pool': debug
        }

        self._session = dict(m=dict(),s=dict())

        for db in dbs:
            master_schema = schema % (master['user'],master['pass'],master['host'],master['port'],db)
            print master_schema
            engine = create_engine(master_schema, **kwargs)
            session = create_session(engine)
            print 'master: %s' % master_schema

            self._session['m'][db] = session
            self._session['s'][db] = []

            for slave in slaves:
                slave_schema = schema % (slave['user'],slave['pass'],slave['host'],slave['port'],db)
                engine = create_engine(slave_schema, **kwargs)
                session = create_session(engine)
                print 'slave: %s' % slave_schema
                self._session['s'][db].append(session)

    @classmethod
    def instance(cls, debug=False):
        if not hasattr(cls, '_instance'):
            cls._instance = cls(debug)
        return cls._instance

    def get_session(self, db, master=False):
        if not master:
            sessions = self._session['s'][db]
            if len(sessions) > 0:
                return random.choice(sessions)
        return self._session['m'][db]

    def close(self):
        for db in self._session['m']:
            self._session['m'][db].close()
            for session in self._session['s'][db]:
                session.close()

# global
backend = Backend.instance(True)

def model2dict(model):
    if not model:
        return {}
    fields = class_mapper(model.__class__).columns.keys()
    return dict((col, getattr(model, col)) for col in fields)

def model_to_dict(func):
    def wrap(*args, **kwargs):
        ret = func(*args, **kwargs)
        return model2dict(ret)
    return wrap

def models_to_list(func):
    def wrap(*args, **kwargs):
        ret = func(*args, **kwargs)
        return partial(map, model2dict)(ret)
    return wrap

