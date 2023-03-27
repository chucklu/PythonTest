from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def useincludetest(request):
    return HttpResponse("这是应用testinclude下的useincludetest函数响应")