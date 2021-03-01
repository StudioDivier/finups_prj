# Generated by Django 3.1.7 on 2021-03-01 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0013_auto_20210301_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='banks',
            name='commission',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=11, verbose_name='Комиссия'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientsentity',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 23, 8, 37, 268765), verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='clientsindividual',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 23, 8, 37, 268765), verbose_name='Дата добавления'),
        ),
    ]