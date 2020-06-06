from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


# 博客文章数据类型
# 包括:文章作者,文章标题,文章正文,文章创建时间,文章更新时间
class ArticlePost(models.Model):
    # 文章作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('标题', max_length=100)
    body = models.TextField('正文')

    created = models.DateTimeField('创建时间', default=timezone.now)
    updated = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])
