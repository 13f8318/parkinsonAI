# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-22 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Psubjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_name', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('doc', models.FileField(default='Doc/None/No-doc.pdf', upload_to='Doc/')),
            ],
        ),
    ]
