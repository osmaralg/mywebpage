# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2020-01-31 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0002_auto_20200131_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(default='static/img/field.jpg', upload_to='static/img/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='static/img/field.jpg', upload_to='static/img/'),
        ),
    ]
