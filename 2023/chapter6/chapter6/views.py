from django.shortcuts import render
from datetime import datetime
from django.template.response import TemplateResponse
from chapter6.models import score
from django.core.paginator import Paginator

def getTime(request):
    return render(request, 'myTemplate.html', {'time': datetime.now()})

def getTimeByTemplateResponse(request):
    return TemplateResponse(request, 'myTemplate.html', {'time': datetime.now()})

def getTable(request):
    table=[
        ['a','b','c'],
        ['d','e','f'],
        ['g','h','i']   
    ]
    return render(request, 'table.html',{'data':table})

def useTemplatePaginator(request):
    data=score.objects.all()
    paginator=Paginator(data,10)
    page=request.GET.get('page',1)
    data=paginator.get_page(page)
    return render(request, 'pageTemplate.html',{'scores':data})