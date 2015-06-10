# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0005_auto_20150524_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlarmStock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('goal_price', models.IntegerField()),
                ('alarm_user', models.ForeignKey(related_name='alarm_user', to=settings.AUTH_USER_MODEL)),
                ('stock_code', models.ForeignKey(to='stock.Stock')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweet_id', models.CharField(max_length=30)),
                ('user', models.ForeignKey(related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
