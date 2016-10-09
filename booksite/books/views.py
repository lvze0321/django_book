#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Book
from django.views.generic import View
# Create your views here.

#表单处理
def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html',{'books':books,'query':q})
#        message = 'You searched for : %s'%request.GET['q']
    else:
#        return HttpResponse('Please submit a search term')
#        message = 'You submitted an empty form.'
         return render_to_response('search_form.html',{'error':True})
    
#    return HttpResponse(message)
        
def search1(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',{'books':books,'query':q})

    return render_to_response('search_form1.html',{'errors':errors})

#url 包含

def aaa(request,test):
    test = str(test)
    s = 'URL include test : %s'%test
    return HttpResponse(s)


