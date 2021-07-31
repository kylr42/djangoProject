from django.urls import path
from django.views.decorators.cache import cache_page

from news.views import *

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),


    path('', HomeNews.as_view(), name='home'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
    path('news/<slug:slug>/', news_detail, name='news'),
    path(
         'category/<slug:slug>/',
         NewsByCategory.as_view(extra_context={'title': 'Тайтл'}),
         name='category'
     ),
]
