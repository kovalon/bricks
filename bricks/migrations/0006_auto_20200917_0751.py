# Generated by Django 3.1.1 on 2020-09-17 04:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bricks', '0005_auto_20200917_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bricks',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 17, 7, 51, 20, 478472)),
        ),
    ]
