from django import forms
from comment.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        # 因为模型中的两个外键将通过视图逻辑自动填写,
        # 所以这里只需要提交body就足够了
        model = Comment
        fields = ['body']
