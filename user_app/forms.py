from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models


class SignStageOne(forms.Form):
    email = forms.EmailField(max_length=100,
                             label='',
                             widget=forms.TextInput(attrs={
                                 'class': 'sign-form',
                                 'name': 'email',
                                 'id': 'email',
                                 'placeholder': 'Электронная почта',
                             }))
    phone = forms.IntegerField(
                             label='',
                             widget=forms.TextInput(attrs={
                                 'class': 'sign-form',
                                 'name': 'phone',
                                 'placeholder': 'Номер телефона',
                                 'value': '+7',
                             }))

    username = forms.CharField(max_length=100,
                             label='',
                             widget=forms.TextInput(attrs={
                                 'class': 'sign-form',
                                 'name': 'username',
                                 'placeholder': 'Имя',
                             }))

    password = forms.CharField(max_length=100,
                             label='',
                             widget=forms.PasswordInput(attrs={
                                 'class': 'sign-form',
                                 'name': 'password',
                                 'placeholder': 'Пароль',
                             }))

    password2 = forms.CharField(max_length=100,
                               label='',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'sign-form',
                                   'name': 'password2',
                                   'placeholder': 'Повтор пароля',
                               }))

    class Meta:
        model = User
        fields = ['email', 'phone', 'username', 'password1', 'password2']

