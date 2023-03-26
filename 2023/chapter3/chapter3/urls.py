"""chapter3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.urls import re_path
from . import views
from testinclude import views as subViews
sub=[path("sub/",subViews.useincludetest)]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("root1/",include('testinclude.urls')),
    path("root2/",subViews.useincludetest),
    path("root3/",include(sub)),
    re_path("^[A-Za-z]+$",views.CharInUrl),
    re_path("^[0-9]{5,}$",views.NumberInUrl),
    path("data1/<urlData>/",views.getData),
    path("data2/<Data1>/<Data2>",views.getData2),
    path("data3/<str:data>",views.getData3),
    path("data4/<int:data>",views.getData4),
    re_path("^redata/(?P<urlData>[a-z0-9]+)$",views.getData),
    path("default/<data>",views.getDefaultData),
    path("default/",views.getDefaultData),
    path("exdata/<data>",views.getExData,{"exdata":"2233"}),
    path("rev/abc",views.getUrlNoParam,name="urlNoPara"),
    path("rev2/<data>",views.getUrlArgs,name="UrlArgs"),
    path("rev3/<data>",views.getUrlKWArgs,name="UrlKwargs"),
    path("rev4/",views.getViewUrl)
]
