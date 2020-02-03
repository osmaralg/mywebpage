# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2020-02-03 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0006_auto_20200201_0036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=42)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=42)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default='No title', max_length=42),
        ),
        migrations.AlterField(
            model_name='project',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sampleapp.Author'),
        ),
        migrations.AlterField(
            model_name='project',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sampleapp.Category'),
        ),
        migrations.AddField(
            model_name='project',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sampleapp.Language'),
        ),
    ]
