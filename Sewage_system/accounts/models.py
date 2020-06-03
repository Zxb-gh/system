from django.db import models
from utils import constants


class User(models.Model):
    """工作人员表"""

    name = models.CharField('姓名', max_length=32)
    username = models.CharField('账户号', max_length=64)
    password = models.CharField('密码', max_length=255)
    level = models.SmallIntegerField('级别',
                                     default=constants.LEVEL_ORDINARY,
                                     choices=constants.LEVEL_CHOICES)

    # is_valid = models.BooleanField('是否有效', default=True)
    login_status = models.BooleanField('登陆状态', default=False)
    # login_frequency = models.IntegerField('登陆次数', default=0)

    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    # updated_at = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        db_table = 'administration_user'
