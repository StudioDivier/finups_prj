# Generated by Django 3.1.7 on 2021-03-01 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0004_auto_20210301_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callbackrequests',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 16, 55, 57, 229677), verbose_name='Время заявки'),
        ),
    ]
