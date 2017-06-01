# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20161227_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=127)),
                ('summary', models.CharField(max_length=4095)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('author', models.ForeignKey(default=None, to='api.Account', null=True)),
                ('category', models.ForeignKey(default=None, to='api.Category', null=True)),
                ('facts', models.ManyToManyField(to='api.Fact')),
                ('hashtags', models.ManyToManyField(to='api.Hashtag')),
            ],
        ),
        migrations.AddField(
            model_name='notification',
            name='thread',
            field=models.ForeignKey(default=None, to='api.Thread', null=True),
        ),
        migrations.AddField(
            model_name='civi',
            name='thread',
            field=models.ForeignKey(default=None, to='api.Thread', null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='categories',
            field=models.ManyToManyField(related_name='user_categories', to='api.Category'),
        ),
        migrations.AddField(
            model_name='thread',
            name='num_civis',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='thread',
            name='num_solutions',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='thread',
            name='num_views',
            field=models.IntegerField(default=0),
        ),
    ]
