# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-21 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='score',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='user',
        ),
        migrations.AddField(
            model_name='rate',
            name='content',
            field=models.CharField(max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rate',
            name='design',
            field=models.CharField(max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rate',
            name='post',
            field=models.ManyToManyField(to='awards.Post'),
        ),
        migrations.AddField(
            model_name='rate',
            name='usability',
            field=models.CharField(max_length=2),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
