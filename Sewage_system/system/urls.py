from django.conf.urls import url

from system import views

urlpatterns = [
    # 验证码
    url(r'^verify/code/$', views.verify_code, name='verify_code'),
    url(r'^matlpotlib/png/$', views.matplotlib_png, name='matplotlib_png'),
]
