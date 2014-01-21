import http

params ={
  'key':'1234hl1k123jlh123jj',
  'client':'android',
  'version':'3.1.3',
  'uuid':'8ee6dc16c595a15f'
}

def get_by_id(id):
    print "==================================="
    url = "https://api.umanoapp.com/v1/clip/%s?"%id
    try:
        res = http.sync_request(url, params)
        import pdb;pdb.set_trace()
        print res['download_url']
        print res['source_url']
        print res['name']
        print "==================================="
    except:
        print "=========error     ================"
        pass


l = [
    '52dab3b783766e5998101626',
    '5096e8e90c917613f5197814',
    '52dcf26183766e5998102951',
    '52dab3b783766e5998101626',
]

for o in l:
    get_by_id(o)

catagraty = [
    '5163b69b6e5534f07c000002',
    '50b71fa5fe4de4eda35d022e',
    '5067b2930f4dfcd2dce0d163',
    '',
]

def get_by_ids(label_id):
    print "==================================="
    url = "https://api.umanoapp.com/v1/label/%d/clips"%label_id
    try:
        res = http.sync_request(url, params)
        import pdb;pdb.set_trace()
        print res['download_url']
        print res['source_url']
        print res['name']
        print "==================================="
    except:
        print "=========error     ================"
        pass

