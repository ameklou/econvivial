# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-01 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conseil', '0002_post_audio_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='document',
            field=models.FileField(default=1, upload_to='document'),
            preserve_default=False,
        ),
    ]
