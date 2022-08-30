import requests
from requests.structures import CaseInsensitiveDict

def callPaul(num, counter):
    url_pacs = "http://10.65.15.141:3100/api/rank"
    # url = "http://10.65.15.159:3100/api/rank"
    cnt = counter.id
    if (cnt == 1):
        name = 'Schalter 1'
    elif (cnt == 2): 
        name = 'Schalter 2'
    else:
        name = 'Schalter 3'
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data = '{"ticket": "# %d", "room": "%s"}' % (num, name)
    resp = requests.post(url_pacs, headers=headers, data=data)
