# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160129_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='XArticle',
            fields=[
                ('publishable_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.Publishable')),
                ('content', models.TextField(default=b'', verbose_name='Content')),
            ],
            options={
                'verbose_name': 'XArticle',
                'verbose_name_plural': 'XArticles',
            },
            bases=('core.publishable',),
        ),
    ]
