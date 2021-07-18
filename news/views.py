from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category
from .forms import NewsForm


def index(request):
	news = News.objects.all()
	context = {
		'news': news,
		'title': 'Список новостей',
	}
	return render(request, 'news/index.html', context)


def get_category(request, category_id):
	news = News.objects.filter(category_id=category_id)
	category = get_object_or_404(Category, pk=category_id)
	context = {
		'news': news,
		'category': category,
	}
	return render(request, 'news/category.html', context)


def get_news(request, news_id):
	news_item = get_object_or_404(News, pk=news_id)
	return render(request, 'news/get_news.html', {'news_item': news_item})


def add_news(request):
	if request.method == 'POST':
		form = NewsForm(request.POST)
		if form.is_valid():
			# var = form.cleaned_data
			# var = News.objects.create(**form.cleaned_data)
			# return redirect('news', var.pk)
			news = form.save()
			return redirect(news)
	else:
		form = NewsForm()
	return render(request, 'news/add_news.html', {'form': form})
