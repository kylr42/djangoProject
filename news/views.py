from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.contrib import messages

from .models import News
from .forms import NewsForm, UserRegisterForm, UserLoginForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})
# class UserRegister(CreateView):
#     form_class = UserRegisterForm
#     template_name = 'news/register.html'
#     success_url = reverse_lazy('login')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно авторизовались!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка авторизации')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')


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
    extra_context = {'title': 'Список новостей'}
    paginate_by = 5
    queryset = News.objects.filter(is_published=True).select_related('category')


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
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return News.objects.filter(
            is_published=True,
            category_id=self.kwargs['category_id']
        ).select_related('category')


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
class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/news_create.html'
    # success_url = reverse_lazy('home')
    login_url = '/admin/'
    # raise_exception = True
