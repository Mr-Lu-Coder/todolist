from django.shortcuts import redirect, render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from list.forms import ExistingListItemForm, ItemForm
from list.models import List
from list import controller
import logging.config
logger = logging.getLogger('list')

def tmp_home(request):
    return render(request, 'tmphome.html', {'form': ItemForm()})


def home_page(req):
    if req.method == 'GET':
        form = ItemForm(data=req.POST)
        try:
            if req.session['islogin']:
                if req.session['role']:
                    logger.info('管理员登录')
                    logger.info('管理员' + req.session['user_info']['name'] + '登录')
                    lists = controller.list_all()
                    logger.info('')
                    return render_to_response('home.html', locals(), context_instance=RequestContext(req))
                else:
                    # print(req.session['role'])
                    logger.info('不是管理员，')
                    userinfo = req.session['user_info']
                    lists = controller.list_user(userinfo)
                    return render_to_response('home.html', locals(), context_instance=RequestContext(req))
            else:
                logger.info('当前没有登录')
                return render_to_response('welcome.html', locals(), context_instance=RequestContext(req))
        except Exception as err:
            logger.error(err)
            req.session['islogin'] = False
            #msg = '请登录'
            logger.info('当前没有登录')
            return render_to_response('welcome.html', locals(), context_instance=RequestContext(req))
    else:
        pass


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})





def add_item(req):
    pass

def del_item(req):
    pass

def update_item(req):
    pass

def add_list(req):
    pass

def del_lsit(req):
    pass

def update_list(req):
    pass



#账户验证！！！！！！
def view_list(req, list_id):
    if not req.session['islogin']:
        raise Http404("Page does not exist!")
    # 获取用户当前的数据
    lists = controller.list_user(req.session['user_info'])
    curlist = List.objects.get(id=list_id)
    form = ItemForm()
    if req.method == 'POST':
        form = ExistingListItemForm(for_list=curlist, data=req.POST)
        if form.is_valid():
            form.save()
            return redirect(curlist)
    return render_to_response('list.html', locals(), context_instance=RequestContext(req))

