# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_alarmstock_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockInform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('per', models.FloatField()),
                ('pbr', models.FloatField()),
                ('cns_per', models.FloatField()),
                ('cns_eps', models.FloatField()),
                ('stock_code', models.ForeignKey(to='stock.Stock')),
            ],
        ),
    ]
