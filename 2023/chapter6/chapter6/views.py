from django.shortcuts import render
from datetime import datetime
from django.template.response import TemplateResponse

def getTime(request):
    return render(request, 'myTemplate.html', {'time': datetime.now()})

def getTimeByTemplateResponse(request):
    return TemplateResponse(request, 'myTemplate.html', {'time': datetime.now()})
