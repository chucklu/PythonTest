from django.shortcuts import render
from datetime import datetime

def getTime(request):
    return render(request, 'myTemplate.html', {'time': datetime.now()})
