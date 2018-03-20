# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Focus',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('note_info', models.CharField(max_length=200, null=True, blank=True)),
                ('info_id', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('code', models.CharField(max_length=6)),
                ('short', models.CharField(max_length=10)),
                ('chg', models.CharField(max_length=10)),
                ('turnover', models.CharField(max_length=255)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('highs', models.DecimalField(max_digits=10, decimal_places=2)),
                ('time', models.DateField(null=True, blank=True)),
            ],
        ),
    ]
