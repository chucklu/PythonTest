from django.shortcuts import render
from django.http import HttpResponse
from goods.models import GoodsCategory
from goods.models import GoodsInfo
from django.core.paginator import Paginator 
# Create your views here.


def getCategoriesWithLastFourGoods():
    # 查询商品分类
    categories = GoodsCategory.objects.all()
    # 从每个分类中获取四个商品
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

#25.2.6 首页页面功能实现
def index(request):

    categoriesWithLastFourGoods = getCategoriesWithLastFourGoods()
    cart_dict = getCartData(request)

    return render(request, 'index.html', {
        'categories': categoriesWithLastFourGoods,
        'cart_goods_list': cart_dict['cart_goods_list'],
        'cart_goods_count': cart_dict['cart_goods_count'],
    })

#25.2.7 商品详细页面功能实现
#本页面除了展示商品的详细信息之外, 分类信息, 当用户点击"加入购物车"按钮, 会将产品信息加入购物车.
def detail(request):
    """商品详细页面"""

    # 获得产品ID
    goods_id = request.GET.get('id', 520)
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

#25.2.8 商品分类页面功能实现
def goods(request):
    """商品展示页面"""

    # 获得当前分类
    cag_id = request.GET.get('cag', 1)
    # 获得当前页码
    page_id = request.GET.get('page', 1)
    # 查询所有数据
    goods_data = GoodsInfo.objects.filter(goods_cag_id=cag_id)
    # 数据分页
    paginator = Paginator(goods_data, 12)
    # 获得当前页码数据
    page_data = paginator.page(page_id)
    # 查询商品分类
    categories = GoodsCategory.objects.all()
    # 查询当前商品分类
    current_cag = GoodsCategory.objects.get(id=cag_id)

    # 读取购物车商品列表
    cart_dict = getCartData(request)

    return render(request, 'goods.html', {'page_data': page_data,
                                          'categories': categories,
                                          'current_cag': current_cag,
                                          'cart_goods_list': cart_dict['cart_goods_list'],
                                          'cart_goods_count': cart_dict['cart_goods_count'],
                                          'paginator': paginator,
                                          'cag_id': cag_id})