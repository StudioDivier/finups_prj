# Generated by Django 3.1.7 on 2021-03-01 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0014_auto_20210301_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callbackrequests',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 22, 32, 39, 271381), verbose_name='Время заявки'),
        ),
    ]