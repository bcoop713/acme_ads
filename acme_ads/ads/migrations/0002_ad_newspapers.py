# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspapers', '0001_initial'),
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='newspapers',
            field=models.ManyToManyField(to='newspapers.Newspaper'),
            preserve_default=True,
        ),
    ]
