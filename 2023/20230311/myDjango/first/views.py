from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("这是我的第一个Django网页")

def say_hello(request):
    return render(request,"hello.html",{"name":"Chuck"})
