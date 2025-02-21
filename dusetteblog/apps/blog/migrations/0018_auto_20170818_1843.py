# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-18 18:43
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_article_is_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='photo',
        ),
        migrations.AddField(
            model_name='article',
            name='photo_main',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='article',
            name='photo_thumb',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=''),
        ),
    ]
