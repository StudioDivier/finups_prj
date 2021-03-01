# Generated by Django 3.1.7 on 2021-03-01 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_auto_20210301_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='typeuser',
            name='entity',
        ),
        migrations.AddField(
            model_name='clientsentity',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_app.typeuser'),
            preserve_default=False,
        ),
    ]
