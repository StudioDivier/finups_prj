# Generated by Django 3.1.7 on 2021-03-02 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0020_auto_20210302_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 2, 15, 39, 36, 245106), verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='clientsentity',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 2, 15, 39, 36, 244136), verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='clientsentity',
            name='org_bank_bic',
            field=models.CharField(max_length=256, verbose_name='БИК'),
        ),
        migrations.AlterField(
            model_name='clientsentity',
            name='org_bank_cor_acc',
            field=models.CharField(max_length=256, verbose_name='Кор.счет'),
        ),
        migrations.AlterField(
            model_name='clientsindividual',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 2, 15, 39, 36, 245106), verbose_name='Дата добавления'),
        ),
    ]
