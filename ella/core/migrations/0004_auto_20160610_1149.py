# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ella.core.cache.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160129_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='related',
            name='publishable',
            field=ella.core.cache.fields.CachedForeignKey(verbose_name='Publishable', to='core.Publishable'),
        ),
    ]
