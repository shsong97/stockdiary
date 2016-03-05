# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0010_gathering'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockfilter',
            name='invest_point_to',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
