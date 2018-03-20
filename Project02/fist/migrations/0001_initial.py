# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('create_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('sex', models.BooleanField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('comment', models.CharField(max_length=200)),
                ('department', models.IntegerField()),
            ],
        ),
    ]
