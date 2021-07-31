import re

from captcha.fields import CaptchaField
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import News, Comment


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'author', 'category', 'content', 'is_published', ]
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'author': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={"class": "form-control"}),
        help_text='Имя пользователя должно состоять максимум из 150 символов.'
    )
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={"class": "form-control"}
    ))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(
        attrs={"class": "form-control"}
    ))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(
        attrs={"class": "form-control"}
    ))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={"class": "form-control"}
    ))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-input", "placeholder": "Ваше имя"}),
            'email': forms.EmailInput(attrs={"class": "form-input", "placeholder": "Ваша почта"}),
            'body': forms.Textarea(attrs={"class": "form-input", "placeholder": "Комментарий..."}),
        }


class EmailPostForm(forms.Form):
    subject = forms.CharField(
        label='Тема',
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    message = forms.CharField(
        label='Текст',
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 10})
    )
    to = forms.EmailField(
        label='Кому',
        widget=forms.EmailInput({"class": "form-control"})
    )
    captcha = CaptchaField(label='Подтверждение')
