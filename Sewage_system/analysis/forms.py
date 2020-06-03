from utils import constants
from analysis.models import PH, Solid, Metal, An

from django import forms


class SelectCellFrom(forms.Form):
    """处理池选择表单"""
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
        ('氨氮吸收池', CELL_ID_THREE_2)
    )
    sel_cell = forms.CharField(max_length=10, widget=forms.widgets.Select(choices=CELL_ID_CHOICES))


class SendorForm(forms.Form):
    """ 历史查询表单 """
    sendor = forms.CharField(label='用户名', max_length=64)

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean_sendor(self):
        sendor = self.cleaned_data['sendor']
        print()

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        # 获取传感器号 ，不建议使用[]的方式
        sendor = self.cleaned_data['sendor']
        print(sendor)
        return cleaned_data


class AlertForm(forms.Form):
    """ 报警查询表单 """
    sendor = forms.CharField(label='用户名', max_length=64)

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean_sendor(self):
        sendor = self.cleaned_data['sendor']
        print()

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        # 获取传感器号 ，不建议使用[]的方式
        sendor = self.cleaned_data['sendor']
        print(sendor)
        return cleaned_data
