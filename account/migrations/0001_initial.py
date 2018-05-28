# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-28 08:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('location', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('sexe', models.CharField(blank=True, max_length=2, null=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('region', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
