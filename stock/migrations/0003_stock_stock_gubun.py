# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20150524_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='stock_gubun',
            field=models.CharField(default=b'\xec\xbd\x94\xec\x8a\xa4\xed\x94\xbc', max_length=10),
        ),
    ]
