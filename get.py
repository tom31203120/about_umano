import lib.http as http
import logging
logger = logging.getLogger(__name__)

int_keys=[
'gender',
'guid',
'length',
]
str_keys=[
'_id',
'created',
'recorded',
'description',
'download_url',
'download_url_2x',
'image_url',
'name',
'source_name',
'source_id',
'source_url',
'status',
'stream_url',
'stream_url_2x',
'thumbnail_url',
]

params ={
  'key':'1234hl1k123jlh123jj',
  'client':'android',
  'version':'3.1.3',
  'uuid':'8ee6dc16c595a15f'
}


from orm import orm
from pprint import pprint
catagraty = orm.label.get_all()
pprint(catagraty)

def construct_data(data):
    one = {}
    if data.has_key('05x'):
        one['has_05x'] = 1 if data['05x'] else 0
    else:
        one['has_05x'] = 0

    if data.has_key('05x'):
        one['has_2x']  = 1 if data['2x'] else 0
    else:
        one['has_2x'] = 0

    for key in str_keys:
        one[key] = data[key] if data.has_key(key) else ''
    for key in int_keys:
        one[key] = data[key] if data.has_key(key) else 0

    #pprint(one)
    return one

def get_by_ids(label):
    print "start==================================="+label['name']

    url = "https://api.umanoapp.com/v1/label/%s/clips"%label['_id']
    try:
        res = http.sync_request(url, params)
        #import pdb;pdb.set_trace()
        while(True):
            data = res['data']
            for one in data:
                orm.umano.add(construct_data(one))
            if not res['continue']:
                break
            url = "https://api.umanoapp.com"+res['continue']+"&key=1234hl1k123jlh123jj&client=android&version=3.1.3&uuid=8ee6dc16c595a15f"
            res = http.sync_request_1(url)
        print "end ==================================="+label['name']
    except Exception as e:
        logger.error('%s\n%s\n', url, str(e))
        print "=========error     ================"+label['name']
        pass

catagraty = catagraty[5:]
#get_by_ids(catagraty)
for one in catagraty:
    get_by_ids(one)
