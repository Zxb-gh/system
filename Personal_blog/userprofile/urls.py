from django.conf.urls import url
from userprofile import views

app_name = 'userprofile'    # 正在部署的应用的名称

urlpatterns = [
    url('login/', views.user_login, name='login'),
    url('logout/', views.user_logout, name='logout'),
    url('register/', views.user_register, name='register'),
]
