# Generated by Django 3.1.7 on 2021-03-01 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0002_auto_20210301_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='callbackrequests',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 10, 26, 2, 142058), verbose_name='Время заявки'),
        ),
    ]
