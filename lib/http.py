#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:

import json
import logging

from urllib import quote_plus
from functools import partial
from urlparse import urljoin
from tornado.httputil import url_concat
from tornado import httpclient, gen, options

logger = logging.getLogger(__name__)

DW_TIMEOUT = 10

def make_url(base, params={}):
    str_params = {k: unicode(v).encode('utf8') for k, v in params.iteritems()}
    url = url_concat(base, str_params)
    return url

def sync_request(api_uri, params={}):
    '''
    params is a dict of remote method's arguments
    example:
        sync_request('activity', {'ActivityName:"每日登录送积分"'})
    '''
    url = make_url(api_uri, params)
    http_client = httpclient.HTTPClient()
    try:
        print url
        response = http_client.fetch(url,
                                     method='GET',
                                     request_timeout=DW_TIMEOUT
                                     )
    except httpclient.HTTPError as e:
        logger.error('%s\n%s\n', url, str(e))
    else:
        res = json.loads(response.body)
        if res['error'] == 'E_OK':
            return res['result']
        else:
            logger.error('%s\n%s\n', url, res['msg'])
    finally:
        http_client.close()

def async_request(uri, params={}, callback=None):
    '''
    params is a dict of remote method's arguments
    '''
    url = make_url(uri, params)

    http_client = httpclient.AsyncHTTPClient()

    _handle_request = partial(handle_request, url=url, callback=callback)

    return http_client.fetch(url,
                             method='GET',
                             callback=_handle_request,
                             request_timeout=DW_TIMEOUT)

def handle_request(response, url, callback):
    if response.error:
        logger.error('%s\n%s\n', url, response.error)
        response.rethrow()
    else:
        res = json.loads(response.body)
        if res['error'] != 'E_OK':
            logger.error('%s\n%s\n', url, res['msg'])
            raise Exception('rpc error:%r' % res)
        else:
            callback(res['result'])

async_task = partial(gen.Task, async_request)
