# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-05-20 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0003_auto_20190513_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecatalogue',
            name='name',
            field=models.CharField(max_length=256, verbose_name='普文目录名'),
        ),
        migrations.AlterField(
            model_name='genebook',
            name='img_name',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='谱书封面'),
        ),
        migrations.AlterField(
            model_name='imgscatalogue',
            name='name',
            field=models.CharField(max_length=256, verbose_name='图像目录名'),
        ),
        migrations.AlterField(
            model_name='ztreecatalogue',
            name='name',
            field=models.CharField(max_length=256, verbose_name='世系目录名'),
        ),
    ]
