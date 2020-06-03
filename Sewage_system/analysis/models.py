from django.db import models
from utils import constants


class Base(models.Model):
    """"""
    cell = models.CharField('处理池编号', max_length=32, )
    is_valid = models.BooleanField('是否有效', default=True)

    class Meta:
        abstract = True


class Solid(Base):
    """固体含量信息表"""
    measure_nub = models.DecimalField('测量数值', max_length=32, default=0, max_digits=5, decimal_places=2)
    name = models.CharField('数据名称', max_length=32, )
    sendor = models.CharField('传感器编号', max_length=32, )
    is_status = models.BooleanField('是否达标', default=True)
    measure_at = models.DateTimeField('测量时间', auto_now_add=True)

    class Meta:
        db_table = 'solid'


class PH(Base):
    """PH信息表"""
    measure_nub = models.DecimalField('测量数值', max_length=32, default=0, max_digits=5, decimal_places=2)
    name = models.CharField('数据名称', max_length=32, )
    sendor = models.CharField('传感器编号', max_length=32, )
    is_status = models.BooleanField('是否达标', default=True)
    measure_at = models.DateTimeField('测量时间', auto_now_add=True)

    class Meta:
        db_table = 'ph'


class Metal(Base):
    """重金属锌含量信息表"""
    measure_nub = models.DecimalField('测量数值', max_length=32, default=0, max_digits=5, decimal_places=2)
    name = models.CharField('数据名称', max_length=32, )
    sendor = models.CharField('传感器编号', max_length=32, )
    is_status = models.BooleanField('是否达标', default=True)
    measure_at = models.DateTimeField('测量时间', auto_now_add=True)

    class Meta:
        db_table = 'metal'


class An(Base):
    """重金属锌含量信息表"""

    measure_nub = models.DecimalField('测量数值', max_length=32, default=0, max_digits=5, decimal_places=2)
    name = models.CharField('数据名称', max_length=32, )
    sendor = models.CharField('传感器编号', max_length=32, )
    is_status = models.BooleanField('是否达标', default=True)
    measure_at = models.DateTimeField('测量时间', auto_now_add=True)

    class Meta:
        db_table = 'an'


class PHAlert(Base):
    """PH报警信息表"""
    name = models.OneToOneField('PH')
    measure_nub = models.DecimalField('测量数值', max_length=32, default=0, max_digits=5, decimal_places=2)
    # name = models.CharField('数据名称', max_length=32, )
    sendor = models.CharField('传感器编号', max_length=32, )
    is_handle = models.BooleanField('是否处理', default=False)
    measure_at = models.DateTimeField('测量时间', auto_now_add=True)

    handle_at = models.DateTimeField('处理时间', auto_now_add=True)
    handle_no = models.SmallIntegerField('处理员工ID')
    status = models.CharField('报警类型', max_length=32)

    class Meta:
        db_table = 'ph_alert'


class SolidAlert(Base):
    """固体处理不合格报警表"""
    name = models.OneToOneField('Solid')
    measure_nub = models.DecimalField('测量数值', max_length=32, default=0, max_digits=5, decimal_places=2)
    # name = models.CharField('数据名称', max_length=32, )
    sendor = models.CharField('传感器编号', max_length=32, )

    is_handle = models.BooleanField('是否处理', default=False)

    handle_at = models.DateTimeField('处理时间', auto_now_add=True)
    measure_at = models.DateTimeField('测量时间', auto_now_add=True)
    handle_no = models.SmallIntegerField('处理员工ID')
    status = models.CharField('报警类型', max_length=32)

    class Meta:
        db_table = 'solid_alert'


class MetalAlert(Base):
    """重金属锌处理不达标报警表"""
    name = models.OneToOneField('Metal')
    measure_nub = models.DecimalField('测量数值', max_length=32, default=0, max_digits=5, decimal_places=2)
    # name = models.CharField('数据名称', max_length=32, )
    sendor = models.CharField('传感器编号', max_length=32, )

    is_handle = models.BooleanField('是否处理', default=False)

    handle_at = models.DateTimeField('处理时间', auto_now_add=True)
    measure_at = models.DateTimeField('测量时间', auto_now_add=True)
    handle_no = models.SmallIntegerField('处理员工ID')
    status = models.CharField('报警类型', max_length=32)

    class Meta:
        db_table = 'metal_alert'


class AnAlert(Base):
    """氨氮处理不达标报警报警表"""
    name = models.OneToOneField('An')
    measure_nub = models.DecimalField('测量数值', max_length=32, default=0, max_digits=5, decimal_places=2)
    # name = models.CharField('数据名称', max_length=32, )
    sendor = models.CharField('传感器编号', max_length=32, )

    is_handle = models.BooleanField('是否处理', default=False)
    measure_at = models.DateTimeField('测量时间', auto_now_add=True)

    handle_at = models.DateTimeField('处理时间', auto_now_add=True)
    handle_no = models.SmallIntegerField('处理员工ID')
    status = models.CharField('报警类型', max_length=32)

    class Meta:
        db_table = 'an_alert'


class Equip(Base):
    """设备表"""

    equip = models.CharField('设备号', max_length=32)
    equip_status = models.SmallIntegerField('处理状态',
                                            default=constants.EQUIPMENT_STATUS_NORMAL,
                                            choices=constants.EQUIPMENT_STATUS_CHOICES)

    status_at = models.DateTimeField('测量时间', auto_now_add=True, null=True, blank=True)

    is_valid = models.BooleanField('是否有效', default=True)

    class Meta:
        db_table = 'equip'


class EquipAlertRecord(Base):
    """设备报警记录表"""
    equip = models.OneToOneField('Equip')

    handle_no = models.SmallIntegerField('处理员工ID')

    status = models.SmallIntegerField('设备报警类型',
                                      default=constants.EQUIP_ALERT_STATUS_ADD,
                                      choices=constants.EQUIP_ALERT_STATUS_CHOICES)

    is_handle = models.BooleanField('是否处理', default=False)

    handle_at = models.DateTimeField('处理时间', auto_now_add=True)

    class Meta:
        db_table = 'equip_alert'


class SelectCell(models.Model):
    """处理池选择"""
    # SELVALUE = (
    #     ('标题', 'first'),
    #     ('内容', 'second'),
    #     ('作者', 'third')
    # )
    CELL_ID_ONE_1 = '1-1'

    CELL_ID_ONE_2 = '1-2'  # 主要分离固体

    CELL_ID_ONE_3 = '1-3'
    CELL_ID_TWO_1 = '2-1'

    CELL_ID_TWO_2 = '2-2'  # 主要吸收重金属
    CELL_ID_TWO_3 = '2-3'  # 重金属吸收后产生的固体

    CELL_ID_THREE_1 = '3-1'  # 吸收氨氮

    CELL_ID_THREE_2 = '3-2'

    CELL_ID_CHOICES = (
        ('初次沉淀池', CELL_ID_ONE_1),
        ('1号过滤池', CELL_ID_ONE_2),
        ('二次沉淀池', CELL_ID_ONE_3),
        ('2号沉淀池', CELL_ID_TWO_1),
        ('重金属吸收池', CELL_ID_TWO_2),
        ('2号过滤池', CELL_ID_TWO_3),
        ('氨氮吸收池', CELL_ID_THREE_1),
        ('氨氮吸收池', CELL_ID_THREE_2),)
    select_cell = models.CharField(max_length=10, choices=CELL_ID_CHOICES)

    class Mate:
        db_table = 'sel_cell'
