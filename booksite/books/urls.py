#coding=utf-8

# url包含

from django.conf.urls import *
from books.models import Publisher
from books import views
from django.views.generic.list import ListView

urlpatterns = patterns('',
        (r'^aaa/$',views.aaa),
        )

urlpatterns += patterns('',
        (r'^publisher/$',ListView.as_view(model = Publisher,template_name = 'publisher_list.html')),
        )
