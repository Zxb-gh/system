# import re

from django import forms
from django.contrib.auth import authenticate, login

from accounts.models import User
from utils.verify import VerifyCode


class UserLoginForm(forms.Form):
    """ 用户登录表单 """
    username = forms.CharField(label='用户名', max_length=64)
    password = forms.CharField(label='密码', max_length=64,
                               widget=forms.PasswordInput,
                               error_messages={
                                   'required': '请输入密码'
                               })
    verify_code = forms.CharField(label='验证码', max_length=4)

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    # def clean_username(self):
    #     """ 验证用户名 hook 钩子函数"""
    #     username = self.cleaned_data['username']
    #     print(username)
    #     # 判断用户名是否为手机号码
    #     pattern = r'^0{0,1}1[0-9]{10}$'
    #     if not re.search(pattern, username):
    #         raise forms.ValidationError('请输入正确的手机号码')
    #     return username

    def clean_verify_code(self):
        """ 验证用户输入的验证码是否正确 """
        verify_code = self.cleaned_data['verify_code']
        if not verify_code:
            raise forms.ValidationError('请输入验证码')
        client = VerifyCode(self.request)
        if not client.validate_code(verify_code):
            raise forms.ValidationError('您输入的验证码不正确')
        return verify_code

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        # 获取用户名和密码 ，不建议使用[]的方式
        # username = cleaned_data['username']

        username = cleaned_data.get('username', None)
        password = cleaned_data.get('password', None)
        if username and password:
            # 查询用户名和密码匹配的用户
            user_list = User.objects.filter(username=username)
            if user_list.count() == 0:
                raise forms.ValidationError('用户名不存在')
            # # 验证密码是否正确
            if not user_list.filter(password=password).exists():
                raise forms.ValidationError('密码错误')
            # if authenticate(username=username, password=password):
            #     raise forms.ValidationError('密码错误')
        return cleaned_data


class UserRegistForm(forms.Form):
    """用户注册表单"""
    username = forms.CharField(label='用户名', max_length=64)
    nickname = forms.CharField(label='昵称', max_length=64)
    password = forms.CharField(label='密码', max_length=64, widget=forms.PasswordInput)
    password_repeat = forms.CharField(label='重复密码', max_length=64, widget=forms.PasswordInput)
    verify_code = forms.CharField(label='验证码', max_length=4)

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.request = request

    def clean_username(self):
        """验证用户名是否被注册"""
        data = self.cleaned_data['username']
        User.objects.filter(username=data)
        if User.objects.filter(username=data).exixts():
            raise forms.ValidationError('用户名已存在')
        return data

    def clean_verify_code(self):
        """验证用户输入的验证码是否正确"""
        verify_code = self.cleaned_data['verify_code']
        if not verify_code:
            raise forms.ValidationError('请输入验证码')
        client = VerifyCode(self.request)
        if not client.validate_code(verify_code):
            raise forms.ValidationError('您输入的验证码不正确')
        return verify_code

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password', None)
        password_repeat = cleaned_data.get('password_repeat', None)
        if password != password_repeat:
            raise forms.ValidationError('两次密码输入不一致')
        return cleaned_data

    def register(self):
        """注册方法"""
        data = self.cleaned_data
        # 1.创建用户
        User.objects.create_user(username=data['username'],
                                 password=data['password'],
                                 nickname='昵称')
        # 2.自动登陆
        user = authenticate(username=data['username'],
                            password=data['password'])
        login(self.request, user)
        return user
