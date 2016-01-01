# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_stockinform'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockFilter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filter_name', models.CharField(max_length=50)),
                ('per_from', models.FloatField()),
                ('per_to', models.FloatField()),
                ('pbr_from', models.FloatField()),
                ('pbr_to', models.FloatField()),
                ('cns_per_from', models.FloatField()),
                ('cns_per_to', models.FloatField()),
                ('cns_eps_from', models.FloatField()),
                ('cns_eps_to', models.FloatField()),
            ],
        ),
    ]
