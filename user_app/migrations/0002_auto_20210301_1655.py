# Generated by Django 3.1.7 on 2021-03-01 13:55

from django.db import migrations, models
import django.db.models.deletion
import user_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientsEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_inn', models.BigIntegerField(verbose_name='ИНН')),
                ('org_form', models.CharField(max_length=8, verbose_name='Форма Организации')),
                ('org_name', models.CharField(max_length=64, verbose_name='Наименование организации')),
                ('org_kpp', models.BigIntegerField(verbose_name='КПП')),
                ('org_ogrn', models.BigIntegerField(verbose_name='ОГРН')),
                ('org_r_account', models.BigIntegerField(verbose_name='Рассчетный счет')),
                ('org_bank_bic', models.BigIntegerField(verbose_name='ИБК')),
                ('org_bank_name', models.CharField(max_length=128, verbose_name='Наименование банка')),
                ('org_bank_cor_acc', models.BigIntegerField(verbose_name='Кор.счет')),
                ('org_gen', models.CharField(max_length=128, verbose_name='Ген.директор')),
                ('org_buh', models.CharField(max_length=128, verbose_name='Гл.бухгалтер')),
                ('charter', models.FileField(blank=True, null=True, upload_to=user_app.models.charterFile, verbose_name='Устав')),
                ('egru', models.FileField(blank=True, null=True, upload_to=user_app.models.egruFile, verbose_name='ЕГРЮ/ЕГРИП')),
                ('certificate', models.FileField(blank=True, null=True, upload_to=user_app.models.certificateFile, verbose_name='Свидетельство')),
                ('gen', models.FileField(blank=True, null=True, upload_to=user_app.models.genFile, verbose_name='Решение о назначении генерального директора')),
                ('buh', models.FileField(blank=True, null=True, upload_to=user_app.models.buhFile, verbose_name='Приказ о назначении главного бухгалтера')),
                ('bal19', models.FileField(blank=True, null=True, upload_to=user_app.models.bal19File, verbose_name='Баланс за 19 год')),
                ('bal20', models.FileField(blank=True, null=True, upload_to=user_app.models.bal20File, verbose_name='Баланс за 20 год')),
            ],
            options={
                'verbose_name': 'Юридическое лицо',
                'verbose_name_plural': 'Юридические лица',
            },
        ),
        migrations.AddField(
            model_name='typeuser',
            name='entity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_app.clientsentity', verbose_name='Юридическое лицо'),
        ),
    ]
