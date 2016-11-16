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
获取所有清单
'''
def list_all():
    try:
        lists = List.objects.all()
        return lists
    except:
        logger.error('获取所有列表错误')
        return -1


'''
获取某一用户的清单
'''
def list_user(userinfo):
    try:
        user = User.objects.get(name=userinfo['name'])
        #print(userinfo['name'])
        lists = user.list_set.all()
        #lists = List.objects.filter(list_name='test01')
        print(lists)
        return lists
    except:
        logger.error('获取用户列表错误')
        return -1


