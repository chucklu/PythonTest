from django.shortcuts import render
from django.shortcuts import redirect
from goods.models import GoodsInfo
from cart.models import OrderGoods
from cart.models import OrderInfo
import time

# Create your views here.

#25.2.7 商品详细页面功能实现
#本页面除了展示商品的详细信息之外, 分类信息, 当用户点击"加入购物车"按钮, 会将产品信息加入购物车.
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

#25.2.9 购物车页面功能实现
def show_cart(request):
    """展示购物车商品"""

    # 读取购物车商品列表
    cart_goods_list = []
    # 商品总数
    cart_goods_count = 0
    # 商品总价
    cart_goods_money = 0.0
    for goods_id, goods_num in request.COOKIES.items():
        if goods_id == 'csrftoken':
            continue

        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        cart_goods.total_money = int(goods_num) * cart_goods.goods_price
        cart_goods_list.append(cart_goods)
        # 累加购物车商品总数
        cart_goods_count = cart_goods_count + int(goods_num)
        # 累计商品总价
        cart_goods_money += int(goods_num) * cart_goods.goods_price

    cart_goods_money = round(cart_goods_money,2)
    return render(request, 'cart.html', {'cart_goods_list': cart_goods_list,
                                         'cart_goods_count': cart_goods_count,
                                         'cart_goods_money': cart_goods_money})

def remove_cart(request):
    """删除购物车商品"""

    # 获得要删除的商品ID
    goods_id = request.GET.get('id', '')
    if goods_id:
        # 获得上一页面地址
        prev_url = request.META['HTTP_REFERER']
        # 写入到 cookie 中
        response = redirect(prev_url)
        # 判断商品是否存在
        goods_count = request.COOKIES.get(goods_id, '')
        if goods_count:
            response.delete_cookie(goods_id)

    return response

#25.2.10 提交订单页面功能实现
def place_order(request):
    """提交订单页面"""

    # 读取购物车商品列表
    cart_goods_list = []
    # 商品总数
    cart_goods_count = 0
    # 商品总价
    cart_goods_money = 0.0
    for goods_id, goods_num in request.COOKIES.items():
        if goods_id == 'csrftoken':
            continue

        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        cart_goods.total_money = int(goods_num) * cart_goods.goods_price
        cart_goods_list.append(cart_goods)
        # 累加购物车商品总数
        cart_goods_count = cart_goods_count + int(goods_num)
        # 累计商品总价
        cart_goods_money += int(goods_num) * cart_goods.goods_price

    freight = 10.0
    cart_goods_money = round(cart_goods_money,2)
    money_to_pay = round(cart_goods_money+freight,2)

    return render(request, 'place_order.html', {'cart_goods_list': cart_goods_list,
                                                'cart_goods_count': cart_goods_count,
                                                'cart_goods_money': cart_goods_money,
                                                'money_to_pay': money_to_pay})

def submit_order(request):
    """保存订单"""

    # 获得订单信息
    addr = request.POST.get('addr', '')
    recv = request.POST.get('recv', '')
    tele = request.POST.get('tele', '')
    extra = request.POST.get('extra', '')

    # 保存订单信息
    order_info = OrderInfo()
    order_info.order_addr = addr
    order_info.order_tele = tele
    order_info.order_recv = recv
    order_info.order_extra = extra
    # 生成订单编号
    order_info.order_id = str(int(time.time() * 1000)) + str(int(time.perf_counter() * 1000000))
    order_info.save()

    # 跳转页面
    response = redirect('/cart/submit_success/?id=%s' % order_info.order_id)

    # 保存订单商品信息
    for goods_id, goods_num in request.COOKIES.items():
        if goods_id == 'csrftoken':
            continue
        # 查询商品信息
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        # 创建订单商品信息
        order_goods = OrderGoods()
        order_goods.goods_info = cart_goods
        order_goods.goods_order = order_info
        order_goods.goods_num = goods_num
        order_goods.save()
        # 删除购物车信息
        response.delete_cookie(goods_id)

    return response


#25.2.11  订单提交成功页面功能实现
def submit_success(request):
    """显示订单结果"""

    order_id = request.GET.get('id')

    order_info = OrderInfo.objects.get(order_id=order_id)
    order_goods_list = OrderGoods.objects.filter(goods_order=order_info)

    # 商品总价
    totla_money = 0
    # 商品总数量
    total_num = 0
    for goods in order_goods_list:
        goods.total_money = goods.goods_num * goods.goods_info.goods_price
        totla_money += goods.total_money
        total_num += goods.goods_num

    return render(request, 'success.html', {'order_info': order_info,
                                            'order_goods_list': order_goods_list,
                                            'totla_money': totla_money,
                                            'total_num': total_num})