# Generated by Django 3.1.1 on 2020-09-17 06:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bricks', '0006_auto_20200917_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bricks',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bricks', to='bricks.building'),
        ),
        migrations.AlterField(
            model_name='bricks',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 17, 9, 21, 29, 868008)),
        ),
    ]
