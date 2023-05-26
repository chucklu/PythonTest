from django.http import HttpResponse
from datetime import date
from django.http import Http404
from django.views import View

def showData(request, urlData):
    d=date.today()
    s=f'urlData = {urlData}<br>Today is {d}'
    return HttpResponse(s)

def testHttp404(request):
    raise Http404('This page does not exist')

def showGetData(request):
    s = f"name is {request.GET['name']}, age is {request.GET['age']}"
    return HttpResponse(s)

class useClassView(View):
    news='使用基于类的视图'
    def get(self, request):
        s = f"{self.news}<br>请求的方法为{request.method}"
        return HttpResponse(s)
    def post(self, request):
        s = f"{self.news}<br>请求的方法为{request.method}"
        return HttpResponse(s)