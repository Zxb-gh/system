from django.conf.urls import url

from analysis import views as views

urlpatterns = [
    # 报警查询
    url(r'^alert/$', views.analysis_alert, name='analysis_alert'),
    # 历史查询
    url(r'^history/$', views.analysis_history, name='analysis_history'),
    # 设备查询
    url(r'^manage/$', views.equip_manage, name='equip_manage'),
    url(r'^cell/$', views.cell, name='cell'),
    url(r"^add/$",views.add),
    url(r"^matlp/1/$",views.matlp_1, name='matlp_1'),
    url(r"^matlp/2/$",views.matlp_2, name='matlp_2'),
    url(r"^matlp/3/$",views.matlp_3, name='matlp_3'),
    url(r"^matlp/4/$",views.matlp_4, name='matlp_4'),
    url(r"^matlp/5/$",views.matlp_5, name='matlp_5'),
    url(r"^matlp/6/$",views.matlp_6, name='matlp_6'),
    url(r"^matlp/7/$",views.matlp_7, name='matlp_7'),
    url(r"^matlp/8/$",views.matlp_8, name='matlp_8'),
    url(r"^matlp/9/$",views.matlp_9, name='matlp_9'),
    url(r"^matlp/10/$",views.matlp_10, name='matlp_10'),
    url(r"^matlp/11/$",views.matlp_11, name='matlp_11'),
    url(r"^matlp/12/$",views.matlp_12, name='matlp_12'),
    url(r'^index/$', views.index, name='index'),

]
