#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
'''
{
    data: {
        05x: true,
        2x: true,
        _id: "52dab3b783766e5998101626",
        created: "2014-01-19T08:17:52.405Z",
        description: "Ever feel like your brain is out to get you? Like it's convincing you to do things that aren't actually in your best interest?",
        displays: 0,
        download_url: "52dab3b783766e5998101626_1390150341/52dab3b783766e5998101626.mp3",
        download_url_2x: "52dab3b783766e5998101626_1390150341/52dab3b783766e5998101626_2x.mp3",
        gender: 0,
        guid: "1502990312",
        image_url: "http://thumbnails.umanoapp.com.global.prod.fastly.net/52dab3b783766e5998101626_1390119472893.jpg",
        length: 327,
        name: "Top 10 Ways To Trick Your Brain Into Doing What You Want",
        popularity: 0.23219573009194328,
        recorded: "2014-01-19T17:01:46.401Z",
        source_id: "50adebea27b80fc4441a511f",
        source_name: "Lifehacker",
        source_url: "http://lifehacker.com/top-10-ways-to-trick-your-brain-into-doing-what-you-wan-1502990312",
        status: "OK",
        stream_url: "52dab3b783766e5998101626_1390150341/stream.m3u8",
        stream_url_2x: "52dab3b783766e5998101626_1390150341/stream_2x.m3u8",
        thumbnail_url: "52dab3b783766e5998101626_1390119475707_thumb.jpg",
}

REATE TABLE `umano_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `has_05x` tinyint(1) DEFAULT '0' COMMENT '是否存在0.5倍速资源',
  `has_2x` tinyint(1) DEFAULT '0' COMMENT '是否存在2倍速资源',
  `_id` varchar(32) NOT NULL COMMENT '资源id',
  `created` varchar(32) NOT NULL COMMENT '创建时间',
  `recorded` varchar(32) NOT NULL COMMENT '录音创建时间',
  `description` varchar(256) NOT NULL COMMENT '简介',
  `download_url` varchar(256) NOT NULL COMMENT 'MP3地址',
  `download_url_2x` varchar(256) NOT NULL COMMENT 'MP3地址',
  `gender` tinyint(1) DEFAULT '0' COMMENT '性别',
  `guid` int(12) NOT NULL DEFAULT '1' COMMENT '文章唯一标示',
  `image_url` varchar(256) NOT NULL COMMENT 'IMG地址',
  `length` int(8) NOT NULL DEFAULT '1' COMMENT '长度',
  `name` varchar(256) NOT NULL COMMENT '文章名称',
  `source_name` varchar(32) NOT NULL COMMENT '来源名字',
  `source_id` varchar(32) NOT NULL COMMENT '来源id',
  `source_url` varchar(256) NOT NULL COMMENT '文章地址',
  `status` varchar(12) NOT NULL COMMENT '状态',
  `stream_url` varchar(256) NOT NULL COMMENT '文章地址',
  `stream_url_2x` varchar(256) NOT NULL COMMENT '文章地址',
  `thumbnail_url` varchar(256) NOT NULL COMMENT '文章地址',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

_id: "5163b69b6e5534f07c000002",
name: "Business",
image_url: "http://thumbnails.umanoapp.com.global.prod.fastly.net/52dafa9483766e5998101912_1390119968152.jpg",
level: 1

CREATE TABLE `label_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_id` varchar(32) NOT NULL COMMENT '类型的id',
  `image_url` varchar(256) NOT NULL COMMENT 'IMG地址',
  `name` varchar(256) NOT NULL COMMENT '文章名称',
  `level` int(8) NOT NULL DEFAULT '1' COMMENT '等级',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

'''
dic = {
        'data': [
            {
                '_id': "5163b69b6e5534f07c000002",
                'name': "Business",
                'image_url': "http://thumbnails.umanoapp.com.global.prod.fastly.net/52dafa9483766e5998101912_1390119968152.jpg",
                'level': 1
                },
            {
                '_id': "50b71fa5fe4de4eda35d022e",
                'name': "Entertainment",
                'image_url': "http://thumbnails.umanoapp.com.global.prod.fastly.net/52dc835a83766e59981025d6_1390257770220.jpg",
                'level': 1
                },
            {
                '_id': "5067b2930f4dfcd2dce0d163",
                'name': "Entrepreneurial",
                'image_url': "http://thumbnails.umanoapp.com.global.prod.fastly.net/52dbb14683766e5998101e1b_1390184812709.jpg",
                'level': 1
                },
            {
                '_id': "5163bda96e5534f07c000004",
                'name': "Facts & History",
                'image_url': "http://thumbnails.umanoapp.com.global.prod.fastly.net/52dd49c583766e5998102e28_1390251157331.jpg",
                'level': 1
                },
            {
                '_id': "5163b7306e5534f07c000003",
                'name': "Lifestyle",
                'image_url': "http://thumbnails.umanoapp.com.global.prod.fastly.net/52dcf59e83766e59981029a2_1390212512469.jpg",
                'level': 1
                },
            {
                '_id': "5067b2930f4dfcd2dce0d164",
                'name': "Scientific",
                'image_url': "http://thumbnails.umanoapp.com.global.prod.fastly.net/52dd8f6383766e5998103320_1390257071611.jpg",
                'level': 1
                },
            {
                '_id': "5271578a892c964659000020",
                'name': "Sports",
                'image_url': "http://thumbnails.umanoapp.com.global.prod.fastly.net/52dc186383766e59981021e4_1390155875828.jpg",
                'level': 1
                },
            {
                '_id': "5067b2930f4dfcd2dce0d162",
                'name': "Technology",
                'image_url': "http://thumbnails.umanoapp.com.global.prod.fastly.net/52dc173083766e59981021de_1390155569371.jpg",
                'level': 1
                },
            {
                '_id': "5067b2930f4dfcd2dce0d165",
                'name': "World & Politics",
                'image_url': "http://thumbnails.umanoapp.com.global.prod.fastly.net/52db901d83766e5998101d89_1390190594326.jpg",
                'level': 1
                }
            ]
}

from orm import orm
data = dic['data']
#import pdb;pdb.set_trace()
#for d in data:
    #print d
    #orm.label.add(d)
print orm.label.get_all()


