from django.http import HttpResponse
from datetime import date
from django.http import Http404
from django.views import View
from django.middleware.csrf import get_token

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
    form_html = f'<form name="input" action="" method="post">' \
                    f'请输入数据：<input type="text" name="data">' \
                    f'<input type="hidden" name="csrfmiddlewaretoken" value="">' \
                    f'<input type="submit" value="提交">' \
                    f'</form>'

    def get(self, request):
        csrf_token = get_token(request)
        form_html = self.form_html.replace('value=""', f'value="{csrf_token}"')
        s = f"{self.news}<br>请求的方法为{request.method}<br>{form_html}"
        return HttpResponse(s)
    
    def post(self, request):
         # Retrieve the posted data
        posted_data = request.POST.get('data', '')
        
        # Render the posted data
        rendered_data = f"您提交的数据为：{posted_data}"

        s = f"{self.news}<br>请求的方法为{request.method}<br>{rendered_data}"
        return HttpResponse(s)
    
class subClassView(useClassView):
    news='使用基于扩展类的视图'
    def get(self, request):
        csrf_token = get_token(request)
        form_html = self.form_html.replace('value=""', f'value="{csrf_token}"')
        s = f"{self.news}<br>重塑的{request.method}<br>{form_html}"
        return HttpResponse(s)