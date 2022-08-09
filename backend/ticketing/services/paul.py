import requests
from requests.structures import CaseInsensitiveDict

def callPaul(num, counter):
    url = "http://10.65.15.159:3100/api/rank"
    cnt = counter.id
    if (cnt == 1):
        name = 'Schalter A'
    else: 
        name = 'Schalter B'
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data = '{"ticket": "# %d", "room": "%s"}' % (num, name)
    resp = requests.post(url, headers=headers, data=data)
