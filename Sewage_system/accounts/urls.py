from django.conf.urls import url
# from django.contrib import admin
from accounts import views

urlpatterns = [
    # 用户登陆
    url(r'^user/login/$', views.user_login, name='user_login'),
    # 退出
    url(r'^user/logout/$', views.user_logout, name='user_logout'),
    # 用户注册
    url(r'^user/register/$', views.user_register, name='user_register'),
]
