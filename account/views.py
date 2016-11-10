from django.shortcuts import render
__author__ = 'lushangqi'


from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django import forms
from account.models import User
from account import controller
import logging
logger = logging.getLogger('account')
# Create your views here.
'''
用户登录
'''
def login(req):
    msg = 'login page'
    if req.method == 'GET':
        logger.info('请求方式错误')
        msg = '请求方式错误'
        return render_to_response('msg.html', locals(), context_instance=RequestContext(req))
    rt = controller.user_login(req.POST)

    if rt:
        req.session['islogin'] = True
        user_info = {}
        user_info['id'] = rt.id
        user_info['name'] = rt.name
        user_info['email'] = rt.email
        if rt.role == '管理员':
            logger.info('管理员 '+rt.name+'登录成功')
            req.session['role'] = True
        else:
            logger.info('普通用户 ' + rt.name + '登录成功')
            req.session['role'] = False
        req.session['user_info'] = user_info
        logger.info('redirect to home')
        print(req.session['role'])
        return HttpResponseRedirect("/")
    else:
        msg = '密码错误！'
        logger.info('密码错误')
        return render_to_response('msg.html', locals(), context_instance=RequestContext(req))

'''
用户登出操作
'''
def logout(req):
    logger.info(req.session['user_info']['name']+ u"登出成功")
    msg = 'logout page'
    req.session['islogin'] = False
    req.session['user_info'] = {}
    req.session['role'] = {}
    return HttpResponseRedirect('/')

def register(req):
    msg = 'register page'
    if req.method == 'GET':
        status = False
        return render_to_response('register.html', context_instance=RequestContext(req))
    else:
        status = True
        rt = controller.user_register(req.POST)
        if rt==1:
            msg = '恭喜注册完成，请直接登录！'

        elif rt == -2:
            msg = '用户名被人注册过了！'
        else:
            msg = '注册失败，请联系管理员'
        return render_to_response('msg.html', locals(), context_instance=RequestContext(req))