# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 08:32
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170423_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
