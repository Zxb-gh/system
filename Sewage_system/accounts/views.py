from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from accounts.forms import UserLoginForm, UserRegistForm
from accounts.models import User
from utils import constants
from utils.verify import VerifyCode


def user_login(request):
    # 第一次访问为GET
    # 第二次访问为POST
    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        print(request.POST)
        client = VerifyCode(request)
        code = request.POST.get('verify_code', None)
        print(type(code))
        rest = client.validate_code(code)
        print('验证结果', rest)
        # 验证表单是否通过
        print(form.is_valid())
        if form.is_valid():
            # 执行登陆
            data = form.cleaned_data

            ## 使用自定义的方式实现登陆
            # 查询用户信息 [MD5]加密算法，不可逆的加密算法1243 -> sdfasvdc
            user = User.objects.get(username=data['username'], password=data['password'])
            # 设置用户ID到session
            request.session[constants.LOGIN_SESSION_ID] = user.id
            # 登陆后的跳转
            return redirect('analysis:index')

        else:
            print(form.errors)
    else:
        form = UserLoginForm(request)
    return render(request, 'login.html', {
        'form': form
    })


def user_logout(request):
    """用户退出"""
    logout(request)
    return redirect('')


def user_register(request):
    """用户注册"""
    if request.method == 'POST':
        form = UserRegistForm(request=request, data=request.POST)
        if form.is_valid():
            # 调用注册方法
            form.register()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = UserRegistForm(request=request)
    return render(request, 'register.html', {
        'form': form
    })
