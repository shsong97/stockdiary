# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_stockfilter'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockinform',
            name='invest_point',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='stockinform',
            name='invest_remark',
            field=models.CharField(default=b'', max_length=10),
        ),
    ]
