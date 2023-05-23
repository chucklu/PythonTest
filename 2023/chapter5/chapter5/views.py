from django.http import HttpResponse
from datetime import date
from django.http import Http404
def showData(request, urlData):
    d=date.today()
    s=f'urlData = {urlData}<br/>Today is {d}'
    return HttpResponse(s)

def testHttp404(request):
    raise Http404('This page does not exist')