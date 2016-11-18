import os
import datetime
from tools import dealData
from tools import config
from list.models import *

import logging
logger = logging.getLogger('root')

'''
有关的数据库操作
'''



'''
获取某一用户的清单，如果该用户是管理员则获得所有用户的清单
'''
def list_all(userinfo, role):
    try:
        if role:
            lists = List.objects.all()
        else:
            user = User.objects.get(name=userinfo['name'])
            #print(userinfo['name'])
            lists = user.list_set.all()
        #lists = List.objects.filter(list_name='test01')
        #print(lists)
        return lists
    except:
        logger.error('获取用户列表错误')
        return -1


