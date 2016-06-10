# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import ella.core.cache.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='format',
            name='master',
            field=ella.core.cache.fields.CachedForeignKey(blank=True, to='photos.Format', help_text='When generating formatted image, use the image formatted to master format instead of the original.Useful when editors crop certain formats by hand and you wish to re-use those coordinates automatically.', null=True, verbose_name='Master'),
        ),
        migrations.AlterField(
            model_name='formatedphoto',
            name='format',
            field=ella.core.cache.fields.CachedForeignKey(to='photos.Format'),
        ),
        migrations.AlterField(
            model_name='formatedphoto',
            name='photo',
            field=ella.core.cache.fields.CachedForeignKey(to='photos.Photo'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='source',
            field=ella.core.cache.fields.CachedForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Source', blank=True, to='core.Source', null=True),
        ),
    ]
