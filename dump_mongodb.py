import requests 
from pymongo import MongoClient
import logging

logger = logging.getLogger('default')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

tag_url = 'https://api.umanoapp.com/v1/label/%s/clips?client=android&version=3.1.3&key=1234hl1k123jlh123jj&uuid=8ee6dc16c595a15f'
continue_url = 'https://api.umanoapp.com%sclient=android&version=3.1.3&key=1234hl1k123jlh123jj&uuid=8ee6dc16c595a15f'

client = MongoClient('localhost', 27017)
db = client['umano_info']

dt = dict(id='5067b2930f4dfcd2dce0d162', name='Technology')
db.tag.update(dt, {"$set": dt}, upsert=True)

tag_continue = []
st = set()

fin_tag = [one for one in db.fin_tag.find()]


def get_umano(tag=dict(id='5067b2930f4dfcd2dce0d162', name='Technology')):
    url = tag_url % tag['id']
    while True:
        try:
            print url
            res = requests.get(url)
            result = res.json()
        except Exception as e:
            print "error url = %s ,e = %s" % (res.url, e)
            break
        else:
            if 0 != result['error']:
                print 'error with %s'%result
                break
            for data in result['data']:
                db.doc.save(data)

                for label in data['labels']:
                    key_label = dict(name=label['name'], id=label['id'])
                    if not db.fin_tag.find_one(key_label) and not db.fail_tag.find_one(
                            key_label) and not db.tag.find_one(key_label):
                        db.tag.insert(key_label)

            c_url = result['continue']
            db[one_tag['name']].update(dict(url=c_url), {"$set": dict(url=c_url)}, upsert=True)
            url = continue_url % c_url

if __name__ == '__main__':
    while db.tag.find():
        tag_continue = []
        one_tag = db.tag.find_one()
        try:
            get_umano(one_tag)
            db.fin_tag.insert(one_tag)
        except Exception as e:
            db.fail_tag.insert(one_tag)
            print "error tag= %s ,e = %s" % (one_tag, e)

        db.tag.remove(one_tag)
