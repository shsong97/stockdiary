# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0003_stock_stock_gubun'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='favorite',
            name='stock_code',
            field=models.ForeignKey(to='stock.Stock'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='stock_user',
            field=models.ForeignKey(related_name='stock_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
