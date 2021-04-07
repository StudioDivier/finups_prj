from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from datetime import datetime
import uuid

from site_app import models as site_model


# Create your models here.
class TypeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_user = models.CharField(name='type_user', verbose_name='Тип пользователя', max_length=16)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return str(self.user.email)


def charterFile(instance, filename):
    return '/'.join([str(instance.id), 'charter', filename])


def egruFile(instance, filename):
    return '/'.join([str(instance.id), 'egru', filename])


def certificateFile(instance, filename):
    return '/'.join([str(instance.id), 'certificate', filename])


def genFile(instance, filename):
    return '/'.join([str(instance.id), 'gen', filename])


def buhFile(instance, filename):
    return '/'.join([str(instance.id), 'buh', filename])


def bal19File(instance, filename):
    return '/'.join([str(instance.id), 'bal19', filename])


def bal20File(instance, filename):
    return '/'.join([str(instance.id), 'bal20', filename])


def bankFile(instance, filename):
    filename = str(uuid.uuid4()) + '.png'
    return '/'.join(['banks', filename])


class ClientsEntity(models.Model):
    org_inn = models.BigIntegerField(name='org_inn', verbose_name='ИНН')
    org_form = models.CharField(name='org_form', verbose_name='Форма Организации', max_length=8)
    org_name = models.CharField(name='org_name', verbose_name='Наименование организации', max_length=64)
    org_kpp = models.BigIntegerField(name='org_kpp', verbose_name='КПП')
    org_ogrn = models.BigIntegerField(name='org_ogrn', verbose_name='ОГРН')
    org_r_account = models.BigIntegerField(name='org_r_account', verbose_name='Рассчетный счет')
    org_bank_bic = models.CharField(name='org_bank_bic', verbose_name='БИК', max_length=256)
    org_bank_name = models.CharField(name='org_bank_name', verbose_name='Наименование банка', max_length=128)
    org_bank_cor_acc = models.CharField(name='org_bank_cor_acc', verbose_name='Кор.счет', max_length=256)
    org_gen = models.CharField(name='org_gen', verbose_name='Ген.директор', max_length=128)
    org_buh = models.CharField(name='org_buh', verbose_name='Гл.бухгалтер', max_length=128)
    # files
    charter = models.FileField(name='charter', verbose_name='Устав', upload_to=charterFile, null=True, blank=True)
    egru = models.FileField(name='egru', verbose_name='ЕГРЮ/ЕГРИП', upload_to=egruFile, null=True, blank=True)
    certificate = models.FileField(name='certificate', verbose_name='Свидетельство', upload_to=certificateFile, null=True, blank=True)
    gen = models.FileField(name='gen', verbose_name='Решение о назначении генерального директора', upload_to=genFile, null=True, blank=True)
    buh = models.FileField(name='buh', verbose_name='Приказ о назначении главного бухгалтера', upload_to=buhFile, null=True, blank=True)
    bal19 = models.FileField(name='bal19', verbose_name='Баланс за 19 год', upload_to=bal19File, null=True, blank=True)
    bal20 = models.FileField(name='bal20', verbose_name='Баланс за 20 год', upload_to=bal20File, null=True, blank=True)
    date_request = models.DateTimeField(name='date_request', verbose_name='Дата добавления', default=datetime.now())

    owner_id = models.ForeignKey(TypeUser, on_delete=models.CASCADE, verbose_name='Владелец')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Юридическое лицо'
        verbose_name_plural = 'Юридические лица'

    def __str__(self):
        return str(self.org_form + ' ' + self.org_name)

    def get_absolute_url(self):
        return reverse('personal:company-detail', kwargs={'slug': self.slug})


class ClientsIndividual(models.Model):
    second_name = models.CharField(name='second_name', verbose_name='Фамилия', max_length=32)
    name = models.CharField(name='name', verbose_name='имя', max_length=32)
    last_name = models.CharField(name='last_name', verbose_name='Отчество', max_length=32)
    city = models.CharField(name='city', verbose_name='Город', max_length=32)
    phone = models.BigIntegerField(name='phone', verbose_name='Телефон')
    email = models.EmailField(name='email', verbose_name='E-mail')
    date_request = models.DateTimeField(name='date_request', verbose_name='Дата добавления', default=datetime.now())

    owner_id = models.ForeignKey(TypeUser, on_delete=models.CASCADE, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Физическое лицо'
        verbose_name_plural = 'Физические лица'

    def __str__(self):
        return str(self.second_name + ' ' + self.name + ' ' + self.last_name)


class Applications(models.Model):
    accept = 'Принято'
    reject = 'Отклонено'
    pending = 'На расмотрении'
    STATUS_LIST = [accept, reject, pending]
    STATUS_TYPE = [
        (accept, 'accept'),
        (reject, 'reject'),
        (pending, 'pending'),
    ]

    type_service = models.CharField(name='type_service', verbose_name='Вид потребности', max_length=32)
    service = models.CharField(name='service', verbose_name='Потребность', max_length=32)
    company = models.ForeignKey(ClientsEntity, on_delete=models.CASCADE, verbose_name='Компания')
    zakon = models.CharField(name='zakon', verbose_name='Закон', max_length=16)
    purchase_number = models.CharField(name='purchase_number', verbose_name='Номер закупки', max_length=128)
    summ = models.DecimalField(name='summ', verbose_name='Сумма', max_digits=15, decimal_places=2)
    contract_price = models.DecimalField(name='contract_price', verbose_name='Цена контракта', max_digits=15, decimal_places=2)
    subj_contract = models.TextField(name='subj_contract', verbose_name='Предмет контракта', max_length=256)
    text_contract = models.TextField(name='text_contract', verbose_name='Предназначение контракта', max_length=256)
    prepaid_expense = models.BooleanField(name='prepaid_expense', verbose_name='Аванс', default=False)
    indisputable_write_off = models.BooleanField(name='indisputable_write_off', verbose_name='Бесспорное списание', default=False)
    date_start = models.DateField(name='date_start', verbose_name='Дата первая', default=datetime.today().strftime('%Y-%m-%d'))
    date_end = models.DateField(name='date_end', verbose_name='Дата вторая', default=datetime.today().strftime('%Y-%m-%d'))
    date_request = models.DateTimeField(name='date_request', verbose_name='Дата добавления', default=datetime.now())

    status = models.CharField(name='status', verbose_name='Статус заявки', choices=STATUS_TYPE, default=pending, max_length=16)

    owner_id = models.ForeignKey(TypeUser, on_delete=models.CASCADE, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return str('Заявка #{} '.format(self.id) + self.owner_id.user.email + ' ' + self.company.org_form + ' ' + self.company.org_name)


class Banks(models.Model):
    name = models.CharField(name='name', verbose_name='Название банка', max_length=64)
    cost = models.DecimalField(name='cost', verbose_name='Стоимость', decimal_places=2, max_digits=11)
    commission = models.DecimalField(name='commission', verbose_name='Комиссия', decimal_places=2, max_digits=11)
    bank_img = models.ImageField(upload_to=bankFile, verbose_name='Логотип банка')

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'

    def __str__(self):
        return str(self.name)


class ApplicationsBank(models.Model):
    user_id = models.ForeignKey(TypeUser, on_delete=models.CASCADE, verbose_name='Ссылка на пользователя')
    app_id = models.ForeignKey(Applications, on_delete=models.CASCADE, verbose_name='Ссылка на заявку')
    bank_id = models.ForeignKey(Banks, on_delete=models.CASCADE, verbose_name='Ссылка на подходщий банк')

    class Meta:
        verbose_name = 'Банк партнер для заявки'
        verbose_name_plural = 'Банки партнеры для заявок'

    def __str__(self):
        return str('Банк по заявке №{} для '.format(self.app_id.id) + self.user_id.user.email + ' {} {}'.format(self.app_id.company.org_form, self.app_id.company.org_name))




