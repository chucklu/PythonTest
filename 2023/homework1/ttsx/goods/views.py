from django.shortcuts import render
from django.http import HttpResponse
from goods.models import GoodsCategory
from goods.models import GoodsInfo
# Create your views here.


def getCategoriesWithLastFourGoods():
    categories = GoodsCategory.objects.all()
    for category in categories:
        category.goods_list = category.goodsinfo_set.all().order_by('-id')[:4]
    print(categories)
    return categories


def getCartData(request):
    cart_dict = {}

    # 读取购物车商品列表
    cart_goods_list = []
    # 商品总数
    cart_goods_count = 0
    for goods_id, goods_num in request.COOKIES.items():
        if goods_id == 'csrftoken':
            continue
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        cart_goods_list.append(cart_goods)
        # 累加购物车商品总数
        cart_goods_count = cart_goods_count + int(goods_num)

    cart_dict['cart_goods_list'] = cart_goods_list
    cart_dict['cart_goods_count'] = cart_goods_count
    return cart_dict


def index(request):

    categoriesWithLastFourGoods = getCategoriesWithLastFourGoods()
    cart_dict = getCartData(request)

    return render(request, 'index.html', {
        'categories': categoriesWithLastFourGoods,
        'cart_goods_list': cart_dict['cart_goods_list'],
        'cart_goods_count': cart_dict['cart_goods_count'],
    })


def detail(request):
    """商品详细页面"""

    # 获得产品ID
    goods_id = request.GET.get('id', 1)
    # 查询该商品
    goods_data = GoodsInfo.objects.get(id=goods_id)
    # 查询商品分类
    categories = GoodsCategory.objects.all()

    # 读取购物车商品列表
    cart_dict = getCartData(request)

    return render(request, 'detail.html', {'categories': categories,
                                           'goods_data': goods_data,
                                           'cart_goods_list': cart_dict['cart_goods_list'],
                                           'cart_goods_count': cart_dict['cart_goods_count'],})
