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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('create_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('sex', models.BooleanField()),
                ('salary', models.DecimalField(max_digits=10, decimal_places=2)),
                ('comment', models.CharField(max_length=200)),
                ('department', models.ForeignKey(to='test01.Department')),
            ],
        ),
    ]
