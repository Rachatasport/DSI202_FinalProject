"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include # new
from django.views.generic import TemplateView
from myapp import views # new
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TemplateView.as_view(template_name="login.html")),
    path('logout/',LogoutView.as_view(template_name='index.html'),name='logout'),
    path('accounts/', include('allauth.urls')), # new
    # path('accounts/', include('django.contrib.auth.urls')), # new
    path('', views.home, name='home'), #new

    path('contact',views.contact),
    path('detail_adaptor',views.detail_adaptor),
    path('detail_case_black',views.detail_case_black),
    path('detail_case_blue',views.detail_case_blue),
    path('detail_case_pink',views.detail_case_pink),
    path('detail_case_red',views.detail_case_red),
    path('detail_case_white',views.detail_case_white),
    path('detail_dock',views.detail_dock),
    path('detail_fabric',views.detail_fabric),
    path('detail_inhaler',views.detail_inhaler),
    path('detail_kit_black',views.detail_kit_black),
    path('detail_kit_white',views.detail_kit_white),
    path('detail_oil',views.detail_oil),
    path('detail_tool',views.detail_tool),
    path('detail_usb',views.detail_usb),
    path('faq',views.faq),
    path('index',views.index),
    path('login',views.login),
    path('payment',views.payment),
    path('shop',views.shop),
    path('shop_accessories',views.shop_accessories),
    path('shop_device',views.shop_device),
    path('shop_filler',views.shop_filler),
    path('shop_promotion',views.shop_promotion),
    path('success',views.success),
    path('track',views.track),


]