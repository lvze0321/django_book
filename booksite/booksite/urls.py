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

#�˴��¾ɰ汾��Django�����޸�
from django.conf.urls import *
from django.contrib import admin
#from booksite.views import hello,current_datetime,hours_ahead,display_meta
from books import views
#import contact.views
admin.autodiscover() #�°汾��������Ҳ�У��д���֤
'''
#�˴��ı�д��Ϊ���°汾��ֱ����[]�������Ƿ�ʹ��url�����ƺ������ԣ���ʼ�Ŀ�''��Ϊͨ����ͼʱʹ�á�
urlpatterns = patterns('',
#   ('^$',my_homepage_view),   �޸�url�����������Ӹ�Ŀ¼���ݿ���������ʾ
    url(r'^admin/', admin.site.urls), #�°汾DjangoĬ�����в���ע�͵������admin
    ('^hello/$',hello),
    ('^time/$',current_datetime),
    (r'^time/plus/(\d{1,2})/$',hours_ahead), #�˴���views��hours_ahead����λ�ò������ã����������Ĳ��ֻ����ַ�����ʽ���ݹ�ȥ
    ('^meta/$',display_meta),#Djangobook ��������ϰ
)
'''

# url�߼�
urlpatterns = patterns('booksite.views',#���ַ�������ʽ�ṩǰ׺
    ('^hello/$','hello'),               #ע������ĺ�����Ϊ�ַ��� 
    ('^time/$','current_datetime'),
    (r'^time/plus/(\d{1,2})/$','hours_ahead'), #�˴���views��hours_ahead����λ�ò������ã����������Ĳ��ֻ����ַ�����ʽ���ݹ�ȥ
#    (r'^time/plus/(?P<offset>\d{1,2})/$','hours_ahead'), #���ָ����?P<name>��ô��Ӧ��view�������յĲ������ֱ���Ϊ��name�������򱨴�
    ('^meta/$','display_meta'),#Djangobook ��������ϰ
)

#���ڱ��ύ��url
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

#url�߼�ʾ��
urlpatterns += patterns('contact.views',
        ('^contact/$','contact'),
        ('^contact1/$','contact1'),
        ('^contact/thanks/$','thanks'),
        )

urlpatterns += patterns('booksite.views',
        (r'^foo/$','foobar_view',{'template_name':'template_name1.html'}),
        (r'^bar/$','foobar_view',{'template_name':'template_name2.html'}),
        )

#url�İ���

urlpatterns += patterns('',
        (r'^app/',include('books.urls'),{'test':1000}),
        )

#ģ��߼�

urlpatterns += patterns('booksite.views',
        (r'^mudel1/$','view_1'),
        (r'^mudel2/$','view_2'),
        )

#ģ�͸߼�����admin

urlpatterns += patterns('',
        url(r'^admin/', admin.site.urls), #�°汾DjangoĬ�����в���ע�͵������admin
        
        )
#���ط�html
urlpatterns += patterns('booksite.views',
        (r'^image/$','my_image'),
        )

#cookies

urlpatterns += patterns('booksite.views',
        (r'^set_color/$','set_color'),
        (r'^get_color/$','get_color'),
        )
