from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def add_cart(request):
    """添加商品到购物车"""

    # 获得商品ID
    goods_id = request.GET.get('id', '')
    if goods_id:
        # 获得上一页面地址
        prev_url = request.META['HTTP_REFERER']
        # 写入到 cookie 中
        response = redirect(prev_url)
        # 判断商品是否存在
        goods_count = request.COOKIES.get(goods_id, '')
        if goods_count:
            goods_count = int(goods_count) + 1
        else:
            goods_count = 1

        response.set_cookie(goods_id, goods_count)

    return response