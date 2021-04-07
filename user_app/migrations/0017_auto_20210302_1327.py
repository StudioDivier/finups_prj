# Generated by Django 3.1.7 on 2021-03-02 10:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0016_auto_20210302_1226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applicationsbank',
            options={'verbose_name': 'Банк партнер для заявки', 'verbose_name_plural': 'Банки партнеры для заявок'},
        ),
        migrations.AddField(
            model_name='applications',
            name='status',
            field=models.CharField(choices=[('Принято', 'Принято'), ('Отклонено', 'Отклонено'), ('На расмотрении', 'На расмотрении')], default='На расмотрении', max_length=16, verbose_name='Статус заявки'),
        ),
        migrations.AlterField(
            model_name='clientsentity',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 2, 13, 27, 21, 540311), verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='clientsindividual',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 2, 13, 27, 21, 540311), verbose_name='Дата добавления'),
        ),
    ]
