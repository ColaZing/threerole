"""djangoProject URL Configuration

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
from django.contrib import admin
from django.urls import path

from bookshop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('delcart/', views.delcart),
    path('catagory/', views.category),
    path('search/', views.search),
    path('detail/', views.detail),
    path('addcart/', views.addcart),
    path('ordersearch/', views.ordersearch),
    path('account/', views.account),
    path('addlike/', views.addlike),
    path('dellike/', views.dellike),
    path('updateaccount/', views.updateaccount),
    path('addaddress/', views.addaddress),
    path('deleteaddress/', views.deleteaddress),
    path('updateorder/', views.updateorder),
    path('exchange/', views.exchange),
    path('createorder/', views.createorder),
    path('checkout/', views.openorder),
]
