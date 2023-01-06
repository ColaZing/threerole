from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin

from bookshop.models import User, Book, BookCategory, Cart, Order, Comment, Collection, Banner, Address, Coupon, \
    CouponCode


# Register your models here.
# 注册用户表
class UserResource(resources.ModelResource):
    class Meta:
        model = User
        # export_order = ('id', 'username', 'password', 'email', 'phone')


class UserAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = UserResource


admin.site.register(User, UserAdmin)


# 注册书籍表
class BookResource(resources.ModelResource):
    class Meta:
        model = Book


class BookAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = BookResource


admin.site.register(Book, BookAdmin)


# 注册购物车表
class CartResource(resources.ModelResource):
    class Meta:
        model = Cart


class CartAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = CartResource


admin.site.register(Cart, CartAdmin)


# 注册订单表
class OrderResource(resources.ModelResource):
    class Meta:
        model = Order


class OrderAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = OrderResource


admin.site.register(Order, OrderAdmin)


# 注册评论表
class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment


class CommentAdmin(ExportMixin, admin.ModelAdmin):
    resource_classes = CommentResource


admin.site.register(Comment, CommentAdmin)


# 注册收藏表
class CollectionResource(resources.ModelResource):
    class Meta:
        model = Collection


class CollectionAdmin(ExportMixin, admin.ModelAdmin):
    resource_classes = CollectionResource


admin.site.register(Collection, CollectionAdmin)


# 注册轮播图表
class BannerResource(resources.ModelResource):
    class Meta:
        model = Banner


class BannerAdmin(ExportMixin, admin.ModelAdmin):
    resource_classes = BannerResource


admin.site.register(Banner, BannerAdmin)


# 注册收货地址表
class AddressResource(resources.ModelResource):
    class Meta:
        model = Address


class AddressAdmin(ExportMixin, admin.ModelAdmin):
    resource_classes = AddressResource


admin.site.register(Address, AddressAdmin)


# 注册优惠券表
class CouponResource(resources.ModelResource):
    class Meta:
        model = Coupon


class CouponAdmin(ExportMixin, admin.ModelAdmin):
    resource_classes = CouponResource


admin.site.register(Coupon, CouponAdmin)


# 注册书籍分类表
class BookCategoryResource(resources.ModelResource):
    class Meta:
        model = BookCategory


class BookCategoryAdmin(ExportMixin, admin.ModelAdmin):
    resource_classes = BookCategoryResource


admin.site.register(BookCategory, BookCategoryAdmin)


# 注册优惠券码表
class CouponCodeResource(resources.ModelResource):
    class Meta:
        model = CouponCode


class CouponCodeAdmin(ExportMixin, admin.ModelAdmin):
    resource_classes = CouponCodeResource


admin.site.register(CouponCode, CouponCodeAdmin)
