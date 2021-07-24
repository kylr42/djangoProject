from django.views.generic import ListView, DetailView, CreateView

from .models import News, Category
from .forms import NewsForm


# def index(request):
# 	news = News.objects.all()
# 	context = {
# 		'news': news,
# 		'title': 'Список новостей',
# 	}
# 	return render(request, 'news/index.html', context)
class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Список новостей'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список новостей'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


# def get_category(request, category_id):
# 	news = News.objects.filter(category_id=category_id)
# 	category = get_object_or_404(Category, pk=category_id)
# 	context = {
# 		'news': news,
# 		'category': category,
# 	}
# 	return render(request, 'news/category.html', context)
class NewsByCategory(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(
            is_published=True,
            category_id=self.kwargs['category_id']
        )


# def get_news(request, news_id):
# 	news_item = get_object_or_404(News, pk=news_id)
# 	return render(request, 'news/get_news.html', {'news_item': news_item})
class ViewNews(DetailView):
    model = News
    pk_url_kwarg = 'news_id'
    template_name = 'news/news_detail.html'
    context_object_name = 'news_item'


# def add_news(request):
# 	if request.method == 'POST':
# 		form = NewsForm(request.POST)
# 		if form.is_valid():
# 			# var = form.cleaned_data
# 			# var = News.objects.create(**form.cleaned_data)
# 			# return redirect('news', var.pk)
# 			news = form.save()
# 			return redirect(news)
# 	else:
# 		form = NewsForm()
# 	return render(request, 'news/add_news.html', {'form': form})
class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/news_create.html'
    # success_url = reverse_lazy('home')
