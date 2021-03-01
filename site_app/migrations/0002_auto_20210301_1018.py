# Generated by Django 3.1.7 on 2021-03-01 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callbackrequests',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='callbackrequests',
            name='phone',
            field=models.BigIntegerField(unique=True, verbose_name='Телефон'),
        ),
    ]
