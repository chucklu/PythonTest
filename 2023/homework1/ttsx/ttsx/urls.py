"""ttsx URL Configuration

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
from django.conf.urls import include
from django.urls import path, re_path
from django.contrib import admin
from goods import views as goods_views  # 导入视图函数

from cart import views as cart_views
from cart.views import show_cart
from cart.views import remove_cart
from cart.views import place_order
from cart.views import submit_order
from cart.views import submit_success

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^index/$', goods_views.index),
    re_path(r'^detail/$', goods_views.detail),
    re_path(r'^cart/add_cart/$', cart_views.add_cart),
    re_path(r'^goods/$', goods_views.goods),
    re_path(r'^cart/show_cart/$', show_cart),
    re_path(r'^cart/remove_cart/$', remove_cart),
    re_path(r'^cart/place_order/$', place_order),
    re_path(r'^cart/submit_order/$', submit_order),
    re_path(r'^cart/submit_success/$', submit_success),
]