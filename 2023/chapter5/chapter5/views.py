from django.http import HttpResponse
from datetime import date
def showData(request, urlData):
    d=date.today()
    s=f'urlData = {urlData}<br/>Today is {d}'
    return HttpResponse(s)