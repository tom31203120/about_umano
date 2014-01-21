#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:

#http://d2wrzndnq0ffz8.cloudfront.net/52db3de683766e5998101b6f_1390129005/52db3de683766e5998101b6f.mp3
from orm import orm
data = dic['data']
#import pdb;pdb.set_trace()
#for d in data:
    #print d
    #orm.label.add(d)
from pprint import pprint
pprint(orm.label.get_all())

    
    
cmd = 'wget %s -c -t 3 -O "%s"' % (url_list[i],downdir+os.sep+song+'.mp3')
os.system(cmd)
