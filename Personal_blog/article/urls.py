from django.conf.urls import url

from article import views

app_name = 'article'    # 正在部署的应用的名称

urlpatterns = [
        # 参数name用于反查url地址,相当于给url起个名字
        url('article_list/', views.article_list, name='article_list'),
        url('article_detail/(?P<id>\d+)/', views.article_detail, name='article_detail'),
        url('article_create/', views.article_create, name='article_create'),
        url('article_safe_delete/(?P<id>\d+)/', views.article_safe_delete, name='article_safe_delete'),
        url('article_update/(?P<id>\d+)/', views.article_update, name='article_update'),
]
