from django.conf.urls import url
from comment import views

app_name = 'comment'    # 正在部署的应用的名称

urlpatterns = [
    url('post_comment/(?P<article_id>\d+)',views.post_comment, name='post_comment'),
]
