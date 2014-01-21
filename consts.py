#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:

# mysql
MYSQL = {
    'master': {
        'host': '192.168.0.121',
        'user': 'ktv',
        'pass': 'hello@ktv',
        'port': 3306
    },
    'slaves': [
        {
            'host': '192.168.0.122',
            'user': 'ktv',
            'pass': 'hello@ktv',
            'port': 3408
        }
    ],
    'dbs': ['common']
}

#debug
MYSQL['master']['host'] = '127.0.0.1'
MYSQL['slaves'] = []

