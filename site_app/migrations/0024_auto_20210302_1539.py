# Generated by Django 3.1.7 on 2021-03-02 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0023_auto_20210302_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callbackrequests',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 2, 15, 39, 36, 242142), verbose_name='Время заявки'),
        ),
    ]
