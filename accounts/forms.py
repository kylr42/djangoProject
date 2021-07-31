from django.contrib.auth.forms import *
from django import forms

from .models import Profile


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={"class": "form-control"}),
        help_text='Имя пользователя должно состоять максимум из 150 символов.'
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        label='Почта',
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Старый пароль',
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    new_password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    new_password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label='Почта',
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )


class UserPasswordConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    new_password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
