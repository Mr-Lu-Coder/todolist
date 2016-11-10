__author__ = 'lushangqi'

from account.models import User
import tools.dealData as fun
import logging
logger = logging.getLogger('account')
def user_login(paras):
    paras = fun.parse_data(paras)
    name = paras.get('name')
    password = fun.mk_md5(paras.get('password'))
    logger.info(name+' is trying login')
    condition = {'name' : name}
    try:
        r = User.objects.get(**condition)
        if r and password == r.password:
            return r
    except:
        logger.error('login error')
        return None

def user_register(paras):
    condition = fun.parse_data(paras)
    del condition['repassword']
    del condition['csrfmiddlewaretoken']
    condition['role'] = '普通用户'
    condition['create_date'] = fun.now()
    condition['password'] = fun.mk_md5(condition['password'])
    for k,v in condition.items():
        print(k,v)
    u = User(**condition)
    try:
        u.save()
    except:
        logger.error('register error')
        return -2
    if u.name:
        logger.info('register success')
        return 1
