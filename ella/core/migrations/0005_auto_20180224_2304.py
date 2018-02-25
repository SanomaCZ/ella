# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160610_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='template',
            field=models.CharField(default=b'category.html', help_text='Template to use to render detail page of this category.', max_length=100, verbose_name='Template', choices=[(b'category.html', 'default (category.html)')]),
        ),
    ]
