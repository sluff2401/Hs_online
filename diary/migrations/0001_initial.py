# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_date', models.DateField(max_length=10, verbose_name=b'Event date in the format yyyy-mm-dd, e.g for the 24th of August 2015, enter 2015-08-24')),
                ('reference', models.CharField(max_length=100)),
                ('text', models.TextField(verbose_name=b'Event details')),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
