#coding=utf-8
"""booksite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

#此处新旧版本的Django做了修改
from django.conf.urls import *
from django.contrib import admin
#from booksite.views import hello,current_datetime,hours_ahead,display_meta
from books import views
#import contact.views
admin.autodiscover() #新版本不添加这句也行，有待考证
'''
#此处的编写较为灵活，新版本中直接用[]，或者是否使用url函数似乎都可以，开始的空''作为通用视图时使用。
urlpatterns = patterns('',
#   ('^$',my_homepage_view),   修改url后如果还想添加根目录内容可以这样表示
    url(r'^admin/', admin.site.urls), #新版本Django默认这行不会注释掉，添加admin
    ('^hello/$',hello),
    ('^time/$',current_datetime),
    (r'^time/plus/(\d{1,2})/$',hours_ahead), #此处向views中hours_ahead传递位置参数，用（）括起来的部分会以字符串形式传递过去
    ('^meta/$',display_meta),#Djangobook 第七章练习
)
'''

# url高级
urlpatterns = patterns('booksite.views',#以字符串的形式提供前缀
    ('^hello/$','hello'),               #注意这里的函数名为字符串 
    ('^time/$','current_datetime'),
    (r'^time/plus/(\d{1,2})/$','hours_ahead'), #此处向views中hours_ahead传递位置参数，用（）括起来的部分会以字符串形式传递过去
#    (r'^time/plus/(?P<offset>\d{1,2})/$','hours_ahead'), #如果指定了?P<name>那么对应的view函数接收的参数名字必须为“name”，否则报错
    ('^meta/$','display_meta'),#Djangobook 第七章练习
)

#用于表单提交的url
urlpatterns += patterns('',
    ('^search-form/$',views.search_form),        
    ('^search/$',views.search),        
    ('^search1/$',views.search1),        
)
'''
urlpatterns += patterns('',
        ('^contact/$',contact.views.contact),
        ('^contact1/$',contact.views.contact1),
        ('^contact/thanks/$',contact.views.thanks),
        )
'''

#url高级示例
urlpatterns += patterns('contact.views',
        ('^contact/$','contact'),
        ('^contact1/$','contact1'),
        ('^contact/thanks/$','thanks'),
        )

urlpatterns += patterns('booksite.views',
        (r'^foo/$','foobar_view',{'template_name':'template_name1.html'}),
        (r'^bar/$','foobar_view',{'template_name':'template_name2.html'}),
        )

#url的包含

urlpatterns += patterns('',
        (r'^app/',include('books.urls'),{'test':1000}),
        )

#模板高级

urlpatterns += patterns('booksite.views',
        (r'^mudel1/$','view_1'),
        (r'^mudel2/$','view_2'),
        )

#模型高级加上admin

urlpatterns += patterns('',
        url(r'^admin/', admin.site.urls), #新版本Django默认这行不会注释掉，添加admin
        
        )
#返回非html
urlpatterns += patterns('booksite.views',
        (r'^image/$','my_image'),
        )

#cookies

urlpatterns += patterns('booksite.views',
        (r'^set_color/$','set_color'),
        (r'^get_color/$','get_color'),
        )
