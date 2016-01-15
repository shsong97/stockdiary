# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0009_auto_20160115_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gathering',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gather_flag', models.CharField(default=b'Y', max_length=1)),
                ('stock_code', models.ForeignKey(to='stock.Stock')),
            ],
        ),
    ]
