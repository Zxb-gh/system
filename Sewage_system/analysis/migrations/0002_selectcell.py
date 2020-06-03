# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-05-21 04:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectCell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_cell', models.CharField(choices=[(0, '初次沉淀池'), (-1, '1号过滤池'), (-1, '二次沉淀池'), (1, '2号沉淀池'), (0, '重金属吸收池'), (-1, '2号过滤池'), (2, '氨氮吸收池'), (1, '氨氮吸收池')], max_length=10)),
            ],
        ),
    ]
