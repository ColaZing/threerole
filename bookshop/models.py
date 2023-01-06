from django.db import models


# Create your models here.

# 用户表
class User(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱')
    phone = models.CharField(max_length=11, verbose_name='手机号')

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


# 书籍表
class Book(models.Model):
    name = models.CharField(max_length=32, verbose_name='书名')
    author = models.CharField(max_length=32, verbose_name='作者')
    price = models.CharField(max_length=32, verbose_name='价格')
    publish = models.CharField(max_length=32, verbose_name='出版社')
    publish_date = models.DateField(verbose_name='出版日期')
    cover = models.CharField(max_length=128, verbose_name='封面')
    desc = models.TextField(verbose_name='简介')
    category = models.CharField(max_length=32, verbose_name='分类')
    sales = models.IntegerField(verbose_name='销量')
    statue = models.CharField(max_length=32, verbose_name='状态')

    class Meta:
        verbose_name = '书籍表'
        verbose_name_plural = verbose_name


# 书籍分类表
class BookCategory(models.Model):
    name = models.CharField(max_length=32, verbose_name='分类名')

    class Meta:
        verbose_name = '书籍分类表'
        verbose_name_plural = verbose_name


# 购物车表
class Cart(models.Model):
    user = models.CharField(max_length=32, verbose_name='用户名')
    book = models.CharField(max_length=32, verbose_name='书名')
    cover = models.CharField(max_length=128, verbose_name='封面')
    price = models.CharField(max_length=32, verbose_name='价格')
    count = models.IntegerField(verbose_name='数量')

    class Meta:
        verbose_name = '购物车表'
        verbose_name_plural = verbose_name


# 订单表
class Order(models.Model):
    user = models.CharField(max_length=32, verbose_name='用户名')
    book = models.CharField(max_length=32, verbose_name='书名')
    count = models.IntegerField(verbose_name='数量')
    price = models.CharField(max_length=32, verbose_name='价格')
    status = models.CharField(max_length=32, verbose_name='状态')
    # ordertime只取日期，不取时间
    ordertime = models.DateField(verbose_name='下单时间')

    class Meta:
        verbose_name = '订单表'
        verbose_name_plural = verbose_name


# 书籍评论表
class Comment(models.Model):
    user = models.CharField(max_length=32, verbose_name='用户名')
    book = models.CharField(max_length=32, verbose_name='书名')
    content = models.TextField(verbose_name='内容')
    time = models.DateTimeField(verbose_name='时间')

    class Meta:
        verbose_name = '书籍评论表'
        verbose_name_plural = verbose_name


# 书籍收藏表
class Collection(models.Model):
    user = models.CharField(max_length=32, verbose_name='用户名')
    book = models.CharField(max_length=32, verbose_name='书名')
    time = models.DateTimeField(verbose_name='时间')

    class Meta:
        verbose_name = '书籍收藏表'
        verbose_name_plural = verbose_name


# 轮播图表
class Banner(models.Model):
    image1 = models.CharField(max_length=128, verbose_name='图片1')
    image2 = models.CharField(max_length=128, verbose_name='图片2')

    class Meta:
        verbose_name = '轮播图表'
        verbose_name_plural = verbose_name


# 收货地址表
class Address(models.Model):
    user = models.CharField(max_length=32, verbose_name='用户名')
    name = models.CharField(max_length=32, verbose_name='收货人')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    address = models.CharField(max_length=128, verbose_name='地址')

    class Meta:
        verbose_name = '收货地址表'
        verbose_name_plural = verbose_name


# 优惠券表
class Coupon(models.Model):
    user = models.CharField(max_length=32, verbose_name='用户名')
    price = models.CharField(max_length=32, verbose_name='价格')
    book = models.CharField(max_length=32, verbose_name='书名')
    time = models.DateTimeField(verbose_name='时间')

    class Meta:
        verbose_name = '优惠券表'
        verbose_name_plural = verbose_name


# 优惠券码表
class CouponCode(models.Model):
    code = models.CharField(max_length=32, verbose_name='优惠券码')
    price = models.CharField(max_length=32, verbose_name='价格')
    book = models.CharField(max_length=32, verbose_name='书名')
    time = models.DateTimeField(verbose_name='时间')

    class Meta:
        verbose_name = '优惠券码表'
        verbose_name_plural = verbose_name