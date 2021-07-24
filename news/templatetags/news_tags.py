from django import template
from django.db.models import Count

from news.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
	cats = Category.objects.annotate(cnt=Count('news'))
	return cats.filter(cnt__gt=0)


# @register.inclusion_tag('news/list_categories.html')
# def show_categories(arg1='Hello', arg2='World'):
# 	categories = Category.objects.all()
# 	return {'categories': categories, 'arg1': arg1, 'arg2': arg2}
