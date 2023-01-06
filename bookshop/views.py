import datetime
from itertools import chain

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from bookshop.models import User, BookCategory, Book, Cart, Banner, Order, Collection, Address, Coupon, CouponCode


# Create your views here.
@csrf_exempt
def nomal(username):
    # 获取书籍分类
    book_category = BookCategory.objects.all()
    # 获取状态是上架的书籍
    book = Book.objects.filter(statue='上架')
    # 获取用户名对应的购物车数量
    cart_count = Cart.objects.filter(user=username).count()
    # 获取用户名对应的购物车信息
    cart = Cart.objects.filter(user=username)
    # 获取用户名对应的购物车的价格乘数量
    cart_price = 0
    for i in cart:
        cart_price += float(i.price) * i.count
    cart_price = cart_price + 19.9
    cart_price = round(cart_price, 2)
    # 获取轮播图的第一条记录
    banner = Banner.objects.first()
    return book_category, book, cart_count, cart, cart_price, banner


@csrf_exempt
def index(request):
    # 判断session是否有内容
    if request.session.get('username'):
        # 获取session
        username = request.session.get('username')
        # 查询user
        user = User.objects.get(username=username)
        book_category, book, cart_count, cart, cart_price, banner = nomal(username)
        return render(request, 'index.html',
                      {'user': user, 'book_category': book_category, 'book': book, 'cart_count': cart_count,
                       'cart': cart, 'cart_price': cart_price, 'banner': banner})
    else:
        return render(request, 'login.html')


# 注册账号
@csrf_exempt
def register(request):
    # 判断请求方式
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # 获取数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        print(username, password, email, phone)
        # 创建user
        try:
            user = User.objects.create(username=username, password=password, email=email, phone=phone)
            user.save()
            # 写入session
            request.session['username'] = user.username
            book_category, book, cart_count, cart, cart_price, banner = nomal(username)
            return render(request, 'index.html',
                          {'user': user, 'book_category': book_category, 'book': book, 'cart_count': cart_count,
                           'cart': cart, 'cart_price': cart_price, 'banner': banner})
        except Exception as e:
            print(e)
            return render(request, 'login.html', {'messagereg': '注册失败'})


# 登录
@csrf_exempt
def login(request):
    # 判断请求方式
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # 获取数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 查询user
        try:
            user = User.objects.get(username=username)
        except:
            return render(request, 'login.html', {'messagelogin': '用户名不存在'})
        # 判断密码
        if user.password == password:
            request.session['username'] = user.username
            book_category, book, cart_count, cart, cart_price, banner = nomal(username)
            return render(request, 'index.html',
                          {'user': user, 'book_category': book_category, 'book': book, 'cart_count': cart_count,
                           'cart': cart, 'cart_price': cart_price, 'banner': banner})
        else:
            return render(request, 'login.html', {'messagelogin': '密码错误'})


# 退出登录
@csrf_exempt
def logout(request):
    # 删除session
    try:
        del request.session['username']
    except:
        pass
    return render(request, 'login.html', {'messagelogin': '退出登录成功'})


# 分类
@csrf_exempt
def category(request):
    # 判断session是否有内容
    if request.session.get('username'):
        # 获取session
        username = request.session.get('username')
        book_category, book, cart_count, cart, cart_price, banner = nomal(username)
        # 获取分类id
        category_id = request.GET.get('id')
        # 通过id获取分类名
        category_name = BookCategory.objects.get(id=category_id)
        name = category_name.name
        # 获取分类下的书籍
        books = Book.objects.filter(category=name)
        # 获取书籍数量
        book_count = books.count()
        return render(request, 'shop.html', {'book_category': book_category, 'book': books, 'cart_count': cart_count,
                                             'cart': cart, 'cart_price': cart_price, 'category_name': name,
                                             "book_count": book_count})


# 搜索书籍
@csrf_exempt
def search(request):
    # 判断session是否有内容
    if request.session.get('username'):
        # 获取session
        username = request.session.get('username')
        book_category, book, cart_count, cart, cart_price, banner = nomal(username)
        # 获取搜索内容
        search = request.POST.get('search')
        # 获取搜索内容
        books = Book.objects.filter(name__contains=search)
        # 获取书籍数量
        book_count = books.count()
        return render(request, 'shop.html', {'book_category': book_category, 'book': books, 'cart_count': cart_count,
                                             'cart': cart, 'cart_price': cart_price, 'category_name': "搜索结果",
                                             "book_count": book_count})


# 书籍详情
@csrf_exempt
def detail(request):
    # 判断session是否有内容
    if request.session.get('username'):
        # 获取session
        username = request.session.get('username')
        book_category, book, cart_count, cart, cart_price, banner = nomal(username)
        # 获取书籍id
        book_id = request.GET.get('id')
        # 通过id获取书籍
        sbook = Book.objects.get(id=book_id)
        return render(request, 'detail.html',
                      {'book_category': book_category, 'book': sbook, 'cart_count': cart_count, 'cart': cart,
                       'cart_price': cart_price})


# 加入购物车
@csrf_exempt
def addcart(request):
    # 判断session是否有内容
    if request.session.get('username'):
        # 获取session
        username = request.session.get('username')
        # 获取书籍id
        book_id = request.GET.get('id')
        # 通过id获取书籍
        sbook = Book.objects.get(id=book_id)
        # 获取用户
        user = User.objects.get(username=username)
        # 判断购物车是否有该书籍
        try:
            cart = Cart.objects.get(book=sbook.name, user=username)
            cart.count += 1
            cart.save()
        except:
            cart = Cart.objects.create(book=sbook.name, user=username, count=1, cover=sbook.cover, price=sbook.price)
            cart.save()
        book_category, book, cart_count, cart, cart_price, banner = nomal(username)
        return render(request, 'detail.html',
                      {'book_category': book_category, 'book': sbook, 'cart_count': cart_count, 'cart': cart,
                       'cart_price': cart_price, 'message': '加入购物车成功'})
    else:
        return render(request, 'login.html', {'messagelogin': '请先登录'})


# 删除购物车
@csrf_exempt
def delcart(request):
    # 获取数据
    username = request.session.get('username')
    id = request.GET.get('id')
    # 删除数据
    Cart.objects.filter(user=username, id=id).delete()
    book_category, book, cart_count, cart, cart_price, banner = nomal(username)
    return render(request, 'index.html',
                  {'book_category': book_category, 'book': book, 'cart_count': cart_count,
                   'cart': cart, 'cart_price': cart_price, 'banner': banner})


# 加入心愿单
@csrf_exempt
def addlike(request):
    # 判断session是否有内容
    if request.session.get('username'):
        # 获取session
        username = request.session.get('username')
        # 获取书籍id
        book_id = request.GET.get('id')
        # 通过id获取书籍
        sbook = Book.objects.get(id=book_id)
        # 获取用户
        user = User.objects.get(username=username)
        # 判断心愿单是否有该书籍
        try:
            like = Collection.objects.get(book=sbook.name, user=username)
        except:
            like = Collection.objects.create(book=sbook.name, user=username, time=datetime.datetime.now())
            like.save()
        book_category, book, cart_count, cart, cart_price, banner = nomal(username)
        return render(request, 'detail.html',
                      {'book_category': book_category, 'book': sbook, 'cart_count': cart_count, 'cart': cart,
                       'cart_price': cart_price, 'message': '加入心愿单成功'})
    else:
        return render(request, 'login.html', {'messagelogin': '请先登录'})


# 删除心愿单
@csrf_exempt
def dellike(request):
    # 获取数据
    username = request.session.get('username')
    id = request.GET.get('id')
    # 删除数据
    Collection.objects.filter(user=username, id=id).delete()
    book_category, book, cart_count, cart, cart_price, banner = nomal(username)
    # 获取心愿单
    like = Collection.objects.filter(user=username)
    return render(request, 'index.html',
                  {'book_category': book_category, 'book': book, 'cart_count': cart_count,
                   'cart': cart, 'cart_price': cart_price, 'banner': banner, 'like': like})


# 搜索时间区间内订单
@csrf_exempt
def ordersearch(request):
    # 判断session是否有内容
    username = 'cola'
    book_category, book, cart_count, cart, cart_price, banner = nomal(username)
    # 获取搜索内容
    begin = request.POST.get('begin')
    end = request.POST.get('end')
    orders = Order.objects.filter(ordertime__range=(begin, end))
    # 获取用户数量
    user_count = User.objects.count()
    # 获取订单数量
    order_count = Order.objects.count()
    # 获取收藏夹数量
    collect_count = Collection.objects.count()
    return render(request, 'accountadmin.html',
                  {'book_category': book_category, 'cart_count': cart_count, 'orders': orders, 'user_count': user_count,
                   'order_count': order_count, 'collect_count': collect_count})


# 个人中心页面
@csrf_exempt
def account(request):
    # 判断session是否有内容
    if request.session.get('username'):
        # 获取session
        username = request.session.get('username')
        book_category, book, cart_count, cart, cart_price, banner = nomal(username)
        # 获取用户
        user = User.objects.get(username=username)
        if username == 'root':
            orders = Order.objects.all()
            # 获取用户数量
            user_count = User.objects.count()
            # 获取订单数量
            order_count = Order.objects.count()
            # 获取收藏夹数量
            collect_count = Collection.objects.count()
            return render(request, 'accountadmin.html',
                          {'book_category': book_category, 'cart_count': cart_count, 'orders': orders,
                           'user_count': user_count, 'order_count': order_count, 'collect_count': collect_count})
        else:
            # 获取收货地址
            address = Address.objects.filter(user=username)
            # 获取订单
            orders = Order.objects.filter(user=username)
            # 获取心愿单
            likes = Collection.objects.filter(user=username)
            # 获取优惠券
            coupons = Coupon.objects.filter(user=username)
            return render(request, 'account.html',
                          {'book_category': book_category, 'cart_count': cart_count, 'cart': cart,
                           'cart_price': cart_price, 'user': user, 'address': address, 'orders': orders,
                           'likes': likes, 'coupons': coupons})
    else:
        return render(request, 'login.html', {'messagelogin': '请先登录'})


# 修改个人信息
@csrf_exempt
def updateaccount(request):
    # 判断session是否有内容
    if request.session.get('username'):
        # 获取session
        username = request.session.get('username')
        # 获取用户
        user = User.objects.get(username=username)
        # 获取数据
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # 修改数据
        user.phone = phone
        user.email = email
        user.password = password
        user.save()
        book_category, book, cart_count, cart, cart_price, banner = nomal(username)
        # 获取收货地址
        address = Address.objects.filter(user=username)
        likes = Collection.objects.filter(user=username)
        # 获取订单
        orders = Order.objects.filter(user=username)
        # 获取优惠券
        coupons = Coupon.objects.filter(user=username)
        return render(request, 'account.html',
                      {'book_category': book_category, 'cart_count': cart_count, 'cart': cart, 'cart_price': cart_price,
                       'user': user, 'message': '修改成功', 'address': address, 'likes': likes, 'orders': orders,
                       'coupons': coupons})
    else:
        return render(request, 'login.html', {'message': '请先登录'})


# 增加收货地址
@csrf_exempt
def addaddress(request):
    # 判断session是否有内容
    if request.session.get('username'):
        # 获取session
        username = request.session.get('username')
        # 获取用户
        user = User.objects.get(username=username)
        # 获取数据
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        # 增加数据
        Address.objects.create(name=name, phone=phone, address=address, user=username)
        book_category, book, cart_count, cart, cart_price, banner = nomal(username)
        # 获取收货地址
        address = Address.objects.filter(user=username)
        likes = Collection.objects.filter(user=username)
        # 获取订单
        orders = Order.objects.filter(user=username)
        # 获取优惠券
        coupons = Coupon.objects.filter(user=username)
        return render(request, 'account.html',
                      {'book_category': book_category, 'cart_count': cart_count, 'cart': cart, 'cart_price': cart_price,
                       'user': user, 'message': '添加成功', 'address': address, 'likes': likes, 'orders': orders,
                       'coupons': coupons})
    else:
        return render(request, 'login.html', {'message': '请先登录'})


# 删除收货地址
@csrf_exempt
def deleteaddress(request):
    # 判断session是否有内容
    if request.session.get('username'):
        # 获取session
        username = request.session.get('username')
        # 获取用户
        user = User.objects.get(username=username)
        # 获取数据
        id = request.GET.get('id')
        # 删除数据
        Address.objects.filter(id=id).delete()
        book_category, book, cart_count, cart, cart_price, banner = nomal(username)
        # 获取收货地址
        address = Address.objects.filter(user=username)
        likes = Collection.objects.filter(user=username)
        # 获取订单
        orders = Order.objects.filter(user=username)
        # 获取优惠券
        coupons = Coupon.objects.filter(user=username)
        return render(request, 'account.html',
                      {'book_category': book_category, 'cart_count': cart_count, 'cart': cart, 'cart_price': cart_price,
                       'user': user, 'message': '删除成功', 'address': address, 'likes': likes, 'orders': orders,
                       'coupons': coupons})
    else:
        return render(request, 'login.html', {'message': '请先登录'})


# 修改订单状态
@csrf_exempt
def updateorder(request):
    # 判断session是否有内容
    if request.session.get('username'):
        # 获取session
        username = request.session.get('username')
        # 获取用户
        user = User.objects.get(username=username)
        # 获取数据
        id = request.GET.get('id')
        # 修改数据
        order = Order.objects.get(id=id)
        order.status = '已退款'
        order.save()
        book_category, book, cart_count, cart, cart_price, banner = nomal(username)
        # 获取收货地址
        address = Address.objects.filter(user=username)
        # 获取订单
        orders = Order.objects.filter(user=username)
        likes = Collection.objects.filter(user=username)
        # 获取优惠券
        coupons = Coupon.objects.filter(user=username)
        return render(request, 'account.html',
                      {'book_category': book_category, 'cart_count': cart_count, 'cart': cart, 'cart_price': cart_price,
                       'user': user, 'message': '修改成功', 'address': address, 'orders': orders, 'likes': likes,
                       'coupons': coupons})
    else:
        return render(request, 'login.html', {'message': '请先登录'})


# 优惠码兑换
@csrf_exempt
def exchange(request):
    # 判断session是否有内容
    if request.session.get('username'):
        # 获取session
        username = request.session.get('username')
        # 获取用户
        user = User.objects.get(username=username)
        # 获取数据
        code = request.POST.get('code')
        # 判断优惠码是否存在优惠券码表中
        coupon = CouponCode.objects.filter(code=code)
        if coupon:
            # 写入优惠券表
            Coupon.objects.create(user=username, price=coupon[0].price, book=coupon[0].book,
                                  time=datetime.datetime.now())
            book_category, book, cart_count, cart, cart_price, banner = nomal(username)
            # 获取收货地址
            address = Address.objects.filter(user=username)
            # 获取订单
            orders = Order.objects.filter(user=username)
            likes = Collection.objects.filter(user=username)
            # 获取优惠券
            coupons = Coupon.objects.filter(user=username)
            return render(request, 'account.html',
                          {'book_category': book_category, 'cart_count': cart_count, 'cart': cart,
                           'cart_price': cart_price, 'user': user, 'message': '兑换成功', 'address': address,
                           'orders': orders, 'likes': likes, 'coupons': coupons})
        else:
            book_category, book, cart_count, cart, cart_price, banner = nomal(username)
            # 获取收货地址
            address = Address.objects.filter(user=username)
            # 获取订单
            orders = Order.objects.filter(user=username)
            likes = Collection.objects.filter(user=username)
            # 获取优惠券
            coupons = Coupon.objects.filter(user=username)
            return render(request, 'account.html',
                          {'book_category': book_category, 'cart_count': cart_count, 'cart': cart,
                           'cart_price': cart_price, 'user': user, 'message': '兑换失败', 'address': address,
                           'orders': orders, 'likes': likes, 'coupons': coupons})


# 创建订单
@csrf_exempt
def createorder(request):
    # 判断session是否有内容
    if request.session.get('username'):
        # 获取session
        username = request.session.get('username')
        # 获取用户
        user = User.objects.get(username=username)
        # 获取数据
        book_category, book, cart_count, cart, cart_price, banner = nomal(username)
        # 取购物车中每个商品的name合并成一个字符串
        book_name = ''
        # 优惠金额
        coupon_price = 0.0
        # 初始化coupon为一个queryset
        coupon = Coupon.objects.filter(user=username, book='全部')
        for i in cart:
            # 购物车的书籍对应销量加1
            book = Book.objects.get(name=i.book)
            book.sales += 1
            book.save()

            book_name += i.book + ','
            # 判断name是否在优惠券表中
            coupona = Coupon.objects.filter(user=username, book=i.book)
            coupon = chain(coupon, coupona)
            if coupona:
                coupon_price += float(coupona[0].price)
        # 判断优惠券表中有没有全部
        couponb = Coupon.objects.filter(user=username, book='全部')
        if couponb:
            coupon_price += float(couponb[0].price)
        # 计算总价
        price = cart_price - coupon_price
        # 保留两位小数
        price = round(price, 2)
        # 计算购物车中的商品数量
        count = 0
        for i in cart:
            count += i.count
        # 生成订单
        Order.objects.create(user=username, book=book_name, count=count, price=price, ordertime=datetime.datetime.now(),
                             status='已下单')
        # 删除购物车中的商品
        Cart.objects.filter(user=username).delete()
        # 获取收货地址
        address = Address.objects.filter(user=username)
        # 获取订单
        orders = Order.objects.filter(user=username)
        likes = Collection.objects.filter(user=username)
        return render(request, 'account.html',
                      {'book_category': book_category, 'cart_count': cart_count, 'cart': cart, 'cart_price': cart_price,
                       'user': user, 'message': '下单成功', 'address': address, 'orders': orders, 'likes': likes})


# 打开订单
@csrf_exempt
def openorder(request):
    # 判断session是否有内容
    if request.session.get('username'):
        # 获取session
        username = request.session.get('username')
        # 获取用户
        user = User.objects.get(username=username)
        # 获取数据
        book_category, book, cart_count, cart, cart_price, banner = nomal(username)
        # 取购物车中每个商品的name合并成一个字符串
        book_name = ''
        # 优惠金额
        coupon_price = 0.0
        # 初始化coupon为一个queryset
        coupon = Coupon.objects.filter(user=username, book='全部')
        for i in cart:
            book_name += i.book + ','
            # 判断name是否在优惠券表中
            coupona = Coupon.objects.filter(user=username, book=i.book)
            coupon = chain(coupon, coupona)
            if coupona:
                coupon_price += float(coupona[0].price)
        # 判断优惠券表中有没有全部
        couponb = Coupon.objects.filter(user=username, book='全部')
        if couponb:
            coupon_price += float(couponb[0].price)
        # 计算总价
        price = cart_price - coupon_price
        # 保留两位小数
        price = round(price, 2)
        # 计算购物车中的商品数量
        count = 0
        for i in cart:
            count += i.count
        return render(request, 'checkout.html',
                      {'book_category': book_category, 'cart_count': cart_count, 'cart': cart, 'cart_price': cart_price,
                       'user': user, 'book_name': book_name, 'count': count, 'price': price, 'coupons': coupon})
