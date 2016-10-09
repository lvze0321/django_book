#coding=utf-8
from django.core.mail import send_mail
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from contact.forms import ContactForm


def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a subject.')
        if not request.POST.get('message',''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                        request.POST['subject'],
                        request.POST['message'],
                        request.POST.get('email','lvze_work@126.com'),
                        ['lvze@cainiaoketang.com'],
                    )
            return HttpResponseRedirect('/contact/thanks')
    return render_to_response('contact_form.html',{'errors':errors,'subject':request.POST.get('subject',''),
        'message':request.POST.get('message',''),
        'email':request.POST.get('email',''),},
        context_instance=RequestContext(request))

def thanks(request):
    return HttpResponse('Thanks!!!')

def contact1(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd  = form.cleaned_data
            send_mail(
                        cd['subject'],
                        cd['message'],
                        cd.get('email','lvze_work@126.com'),
                        ['lvze@cainiaoketang.com'],
                    )
            return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm(initial = {'subject':"I love your site"})
    return render_to_response('contact_form1.html',{'form':form},context_instance = RequestContext(request))
            
