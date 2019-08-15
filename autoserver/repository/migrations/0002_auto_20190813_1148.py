# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-08-13 03:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assetrecord',
            options={'ordering': ('-create_at',), 'verbose_name_plural': '资产记录表'},
        ),
        migrations.AlterField(
            model_name='assetrecord',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='repository.Server'),
        ),
        migrations.AlterField(
            model_name='server',
            name='latest_date',
            field=models.DateField(null=True, verbose_name='最后更新时间'),
        ),
    ]