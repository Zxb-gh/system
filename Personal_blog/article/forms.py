# 引入表单类
from django import forms
# 引入文章模型
from article.models import ArticlePost


# 写文章的表单类
# 在ArticlePost模型中,created和updated字段是自动生成的,不需要填入
# author字段暂时固定为id=1的管理员用户,也不需要填写
# 所以需要填写的就是title和body

class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = ArticlePost
        fields = ('title','body')