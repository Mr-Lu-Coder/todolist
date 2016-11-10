import logging.config
from os import path

import logging
logger = logging.Logger('root')

def mk_md5(s):
    import hashlib
    m = hashlib.md5()
    m.update(s.encode('utf-8'))
    return m.hexdigest()

def parse_data(data):
    data = dict(data)
    for k,v in data.items():
        if isinstance(v, list):
            if len(v)>1:
                data[k] = ','.join(v)
            elif len(v)==1:
                data[k] = v[0]
            else:
                data[k] = ''
        else:
            data[k] = ''
    return data

def now():
    import time
    return time.strftime('%Y-%m-%d %X', time.localtime() )