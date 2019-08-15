import requests

import json
import time
import hashlib

KEY = 'alkdjwqm,ensklhjkrhwfeqnsdah'


def gen_key(ctime):
    key = "{}|{}".format(KEY, ctime)

    md5 = hashlib.md5()
    md5.update(key.encode('utf-8'))

    return md5.hexdigest()


ctime = time.time()

time.sleep(4)
ret = requests.post(
    url='http://127.0.0.1:8000/api/test/?key={}&ctime={}'.format(gen_key(ctime), ctime),
    data=json.dumps({'disk': {}, 'nic': 'xxx'}).encode('utf-8'),
    headers={'content-type': 'application/json'},
)


# ret = requests.post(
#     url='http://127.0.0.1:8000/api/test/?key=790f3e59400ee3e55fbea6006668598d&ctime=1565571603.7346337',
#     data=json.dumps({'disk': {}, 'nic': 'xxx'}).encode('utf-8'),
#     headers={'content-type': 'application/json'},
# )

print(ret.json())
