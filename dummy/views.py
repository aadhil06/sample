from http.client import HTTPResponse
from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
from pickle import GET
from django.contrib.auth.models import auth,User
from .models import Contact
# Create your views here.
def index(request):
    if request.method=="POST":
        usn=request.POST.get('usn','')
        name=request.POST.get('name','')
        sem=request.POST.get('sem','')
        num=request.POST.get('num','')
        mail=request.POST.get('mail','')
        if usn and name and sem and num and mail:
            contact=Contact(usn=usn,name=name,sem=sem,num=num,mail=mail)
            contact.save()
        else:
            return HttpResponse("enter all details")

    return render(request,'index.html')

