# import markdown
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from article.forms import ArticlePostForm
from article.models import ArticlePost
from comment.models import Comment


def article_list(request):
    articles = ArticlePost.objects.all()  # 获取ArticlePost中的所有数据
    context = {'articles': articles}
    return render(request, 'list.html', context)


def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)

    comments = Comment.objects.filter(article=id)
    print(article)
    context = {'article': article, 'comments': comments,}
    return render(request, 'detail.html', context)


# 写文章的视图函数
def article_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的需求
        if article_post_form.is_valid():
            # 保存数据,但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            # 指定数据库中,id=1的用户为作者
            # 如果你进行过删除数据表的操作,可能会找不到id=1的用户
            # 此时请重新创建用户,并传入此用户id
            new_article.author = User.objects.get(id=1)
            # 将新文章保存到数据库中
            new_article.save()
            return redirect('article:article_list')
        else:
            return HttpResponse('表单内容有误,请重新填写')
    # 如果用户请求获取数据
    else:
        # 创建表单实例
        article_post_form = ArticlePostForm()
        context = {'article_post_form': article_post_form}
        return render(request, 'create.html', context)


def article_safe_delete(request, id):
    if request.method == "POST":
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许POST请求")


# 更新文章
def article_update(request,id):
    """
    更新文章的视图函数
    通过
    POST方法提交表单,更新title,body字段
    GET方法进入初始表单页面
    id:是文章的id
    """
    # 获取需要修改的具体文章对象
    article = ArticlePost.objects.get(id=id)
    # 判断用户是否为POST提交表单数据
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的需求
        if article_post_form.is_valid():
            article.title = request.POST.get('title')
            article.body = request.POST.get('body')
            article.save()

            # 完成后返回到修改后的文章中,需要传入文章的id值
            return redirect("article:article_detail",id=id)
        else:
            return HttpResponse('表单内容有误,请重新填写')
    # 如果是get请求
    else:
        article_post_form = ArticlePostForm()
        context = {'article': article, 'article_post_form': article_post_form}
        # 将响应返回到模板中
        return render(request, 'update.html', context)

