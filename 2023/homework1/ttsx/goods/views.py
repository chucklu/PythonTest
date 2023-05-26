from django.shortcuts import render
from django.http import HttpResponse
from goods.models import GoodsCategory
# Create your views here.

def index(request):
    categories =  GoodsCategory.objects.all()
    for category in categories:
        category.goods_list=category.goodsinfo_set.all().order_by('-id')[:4]
    print(categories)
    return render(request, 'index.html',{
        'categories':categories,
    })