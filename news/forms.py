import re

from captcha.fields import CaptchaField
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .admin import NewsAdminForm
from .models import News


# class NewsForm(forms.Form):
# 	title = forms.CharField(max_length=150, label='Название',
# 		widget=forms.TextInput(attrs={"class": "form-control"}))
# 	content = forms.CharField(label='Текст', required=False,
# 		widget=forms.Textarea(attrs={"class": "form-control"}))
# 	is_published = forms.BooleanField(label='Опубликовать', initial=True,
# 		widget=forms.CheckboxInput())
# 	category = forms.ModelChoiceField(empty_label=None, queryset=Category.objects.all(),
# 		label='Категория', widget=forms.Select(attrs={"class": "form-control"}))
class NewsForm(forms.ModelForm):
	class Meta:
		model = News
		fields = ['title', 'content', 'is_published', 'category']
		widgets = {
			'title': forms.TextInput(attrs={"class": "form-control"}),
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


class ContactForm(forms.Form):
	subject = forms.CharField(
		label='Тема',
		widget=forms.TextInput(attrs={"class": "form-control"}),
	)
	message = forms.CharField(label='Текст', widget=forms.Textarea(
		attrs={"class": "form-control", "rows": 10}
	))
	captcha = CaptchaField(label='Подтверждение')

