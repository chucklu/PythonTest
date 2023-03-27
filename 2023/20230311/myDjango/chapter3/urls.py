from django.urls import path,include
from django.urls import re_path
from . import views
#from testinclude import views as subViews
#sub=[path("sub/",subViews.useincludetest)]

urlpatterns =[
    #path("root1/",include('testinclude.urls')),
    #path("root2/",subViews.useincludetest),
    #path("root3/",include(sub)),
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
    path("rev4/",views.getViewUrl),
]