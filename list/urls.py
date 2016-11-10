from django.conf.urls import url

from list import views
import logging
import logging.config
logger = logging.getLogger('list')


urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/$', views.view_list, name='view_list'),
    #url(r'^user\(\d+)/$', views.view_list, name='user_list'),
    url(r'^tmphome$', views.tmp_home, name='tmp_list'),
]

