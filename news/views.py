from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.contrib import messages

from .models import News
from .forms import NewsForm, UserRegisterForm, UserLoginForm, EmailPostForm, CommentForm


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


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    extra_context = {'title': 'Список новостей'}
    paginate_by = 5
    queryset = News.objects.filter(is_published=True).select_related('category')


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
        return News.published.filter(
            category__slug=self.kwargs['slug']
        ).select_related('category')


# class DetailNews(DetailView):
#     model = News
#     pk_url_kwarg = 'slug'
#     template_name = 'news/news_detail.html'
#     context_object_name = 'news_item'
#
#     def get_context_data(self, **kwargs):
#         context = super(DetailNews, self).get_context_data(**kwargs)
#         context['form'] = MyFormClass
#         return context


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/news_create.html'
    # success_url = reverse_lazy('home')
    login_url = '/admin/'
    # raise_exception = True


def news_share(request, slug):
    news_item = get_object_or_404(News, slug=slug)
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                news_url = request.build_absolute_uri(news_item.get_absolute_url())
                subject = f"{news_item.title}"
                message = f"Read {news_item.title} at {news_url}\n\n" \
                          f"comments: {cd['message']}"
                send_mail(subject, message, 'admin@myblog.com',
                          [cd['to']])
                messages.success(request, 'Письмо отправлено!')
                form = EmailPostForm()
            except Exception as e:
                messages.error(request, f'Ошибка отправки - {e}')
        else:
            messages.error(request, 'Ошибка валидации')
    else:
        form = EmailPostForm()
    return render(request, 'news/news_share.html', {'form': form})


def news_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug)
    comments = news_item.comments.filter(status=True)
    new_comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.news = news_item
            new_comment.save()
        else:
            messages.error(request, 'Ошибка валидации')
    else:
        form = CommentForm()
    context = {
        'form': form, 'news_item': news_item,
        'comments': comments, 'new_comment': new_comment,
    }
    return render(request, 'news/news_detail.html', context=context)
