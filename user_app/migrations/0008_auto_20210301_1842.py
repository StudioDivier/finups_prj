# Generated by Django 3.1.7 on 2021-03-01 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0007_auto_20210301_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientsentity',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 18, 42, 0, 302281), verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='clientsindividual',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 18, 42, 0, 302281), verbose_name='Дата добавления'),
        ),
    ]