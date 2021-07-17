from django import forms
from .models import Category


class NewsForm(forms.Form):
	title = forms.CharField(max_length=150, label='Название',
		widget=forms.TextInput(attrs={"class": "form-control"}))
	content = forms.CharField(label='Текст', required=False,
		widget=forms.Textarea(attrs={"class": "form-control"}))
	is_published = forms.BooleanField(label='Опубликовать', initial=True,
		widget=forms.CheckboxInput())
	category = forms.ModelChoiceField(empty_label=None, queryset=Category.objects.all(),
		label='Категория', widget=forms.Select(attrs={"class": "form-control"}))
