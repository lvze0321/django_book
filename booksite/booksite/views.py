#!/usr/bin/python
#coding=utf-8

from django.http import HttpResponse,Http404
import datetime
from django.template import loader,Context,RequestContext
from django.shortcuts import render_to_response,render
#from django.template import Context

#每个视图函数都至少包含一个参数，通常叫request是django.http.HttpResponse的一个实例
def hello(request):
    return HttpResponse("Hello World")

'''
def current_datetime(request):
    now = datetime.datetime.now()
    t = loader.get_template('current_datetime.html')
#    html = "<html><body>It is now %s.</body></html>"%now
    html = t.render({'current_date':now}) #在旧版本中用Context类型
    return HttpResponse(html)
'''
def current_datetime(request):
#    now = datetime.datetime.now()
#    return render_to_response('current_datetime.html',{'current_date':now})
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html',locals())

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    assert False
    html = "<html><body>In %s hours,it will be %s.</body></html>"%(offset,dt)
    return HttpResponse(html)

#Djangobook 第七章练习
def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    path = request.path
    for (k,v) in  values:
        html.append((k,v))
    return render_to_response('meta.html',{'meta_data':html,'request_path':path})

#模板进阶

def custom_proc(request):
    return {'app':'My app',
            'user':request.user,
            'ip_address':request.META['REMOTE_ADDR']
            }

def view_1(request):
    t = loader.get_template('template1.html')
    c = RequestContext(request,{'message':'I am view 1'},
            processors = [custom_proc])
    return HttpResponse(t.render(c))

#在settings中设置custom_proc为全局，所以和view1对比可以不加processors亦可
def view_2(request):
    t = loader.get_template('template2.html')
    c = RequestContext(request,{'message':'I am view 2'})
    return HttpResponse(t.render(c))

def foobar_view(request,template_name):
    return render_to_response(template_name,{})

def my_image(request):
    image_data = open('/home/lvze/image.png','rb').read()
    return HttpResponse(image_data,content_type = "image/png")

def get_color(request):
    if "favorite_color" in request.COOKIES:
        return HttpResponse("Your favorite color is %s"%request.COOKIES['favorite_color'])
    else:
        return HttpResponse("You don't have a favorite color.")

def set_color(request):
    if "favorite_color" in request.COOKIES:
        response = HttpResponse("Your favorite color is %s"%request.GET['favorite_color'])#从表单获取favorite color，如果不想写表单也可以用其他方法测试
        response.set_cookie("favorite_color",request.GET["favorite_color"])
        return response
    else:
        response = HttpResponse("You don't have a favorite color.")
        return response

def login(request):
    if request.method != 'POST':
        raise Http404("only POSTs are allowed")
    try:
        m = Mumber.object.get(username = request.POST['username'])
        if m.password == request.POST['password']:
            request.session['member_id'] = m.id
            return HttpResponseRedirect('/you-are-logged-in/')
    except Member.DoseNotExist:
        return HttpResponse("your username and password didn't match")

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")
