from django.http import HttpResponse
from html import escape

def CharInUrl(request):
    return HttpResponse("视图url只包含大小写字母")

def NumberInUrl(request):
    return HttpResponse("视图url只包含数字")

def getData(requset,urlData):
    return HttpResponse("从URL获取的数据:"+urlData)

def getData2(requset,Data1,Data2):
    return HttpResponse("从URL获取的数据:"+Data1+","+Data2)

def getData3(request,data):
 #   s="使用str转换器,数据为"+data+",类型为"+type(data).__name__
    s=f"使用str转换器,数据为{data},类型为{type(data)}"
    return HttpResponse(escape(s))

def getData4(request,data):
    s="使用int转换器，数据为"+str(data)+"，类型为"+str(type(data))
    return HttpResponse(escape(s))

def getDefaultData(request,data=123):
    return HttpResponse("使用带默认值的参数data=123，当前值"+str(data))

def getExData(request,exdata,ex):
    return HttpResponse("使用带附加数据的参数，数据为"+exdata+",附加值为"+ex)

from django.urls import reverse
def getUrlNoParam(request):
    return HttpResponse("请求的url路径为:"+reverse("urlNoPara"))

def getUrlArgs(request,data):
    return HttpResponse("请求的url路径为:"+reverse("UrlArgs",args=["sadas"]))

def getUrlKWArgs(request,data):
    return HttpResponse("请求的url路径为:"+reverse("UrlKwargs",kwargs={'data':1234}))

def getViewUrl(request):
    return HttpResponse("getUrlKWArgs视图函数的路径为"+reverse(getUrlKWArgs,kwargs={'data':1234}))