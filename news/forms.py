import re

from captcha.fields import CaptchaField
from django import forms
from django.core.exceptions import ValidationError

from .models import News, Comment


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'author', 'category', 'content', 'photo', 'is_published', ]
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
