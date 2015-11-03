# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='To_do',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('priority', models.IntegerField(default=1)),
                ('date', models.DateTimeField(verbose_name=b'Date inputted')),
                ('description', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=20)),
            ],
        ),
    ]
