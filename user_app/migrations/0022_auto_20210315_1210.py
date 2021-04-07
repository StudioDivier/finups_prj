# Generated by Django 3.1.7 on 2021-03-15 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0021_auto_20210302_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='date_end',
            field=models.DateField(default='2021-03-15', verbose_name='Дата вторая'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 15, 12, 10, 2, 760145), verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='date_start',
            field=models.DateField(default='2021-03-15', verbose_name='Дата первая'),
        ),
        migrations.AlterField(
            model_name='clientsentity',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 15, 12, 10, 2, 759143), verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='clientsindividual',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 15, 12, 10, 2, 760145), verbose_name='Дата добавления'),
        ),
    ]