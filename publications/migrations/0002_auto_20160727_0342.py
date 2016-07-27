# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=140, blank=True)),
                ('text', models.TextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('visible', models.BooleanField(default=True)),
                ('project', models.ForeignKey(to='publications.Project', related_name='entries')),
            ],
        ),
        migrations.RemoveField(
            model_name='publication',
            name='project',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
    ]
