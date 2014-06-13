import requests
import os
from pymongo import MongoClient
import logging

logger = logging.getLogger('default')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

client = MongoClient('localhost', 27017)
db = client['umano_info']

base_down_url = "http://d2wrzndnq0ffz8.cloudfront.net/%s"



def d_save(url, path):
    logger.info('fetching %s to %s ', url, path)
    r = requests.get(url)
    with open(path, "wb") as code:
        code.write(r.content)


def down_doc_file(doc={}):
    key_doc = dict(_id=doc['_id'], name=doc['name'])
    if db.down_url.find_one(key_doc) and db.error_down_url:
        return

    try:
        download_url = base_down_url % doc['download_url']
        directory, file_name = doc['download_url'].split('/')

        # if not os.path.exists(directory):
        #     os.makedirs(directory)

        d_save(download_url, file_name)

    except Exception as e:
        db.error_down_url.save(key_doc)
        logger.error('error = %s', e)
    else:
        logger.info('success down %s', download_url)
        db.down_url.save(key_doc)


def get_data():
    for one_doc in db.doc.find():
        down_doc_file(one_doc)

if __name__ == '__main__':
    get_data()
