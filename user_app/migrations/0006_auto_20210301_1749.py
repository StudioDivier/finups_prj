# Generated by Django 3.1.7 on 2021-03-01 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_clientsindividual_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientsentity',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 17, 49, 57, 496998), verbose_name='Дата добавления'),
        ),
        migrations.AddField(
            model_name='clientsindividual',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 17, 49, 57, 496998), verbose_name='Дата добавления'),
        ),
    ]
