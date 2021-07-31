from django.urls import path

from news.views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
    path('news/share/<slug:slug>/', news_share, name='share_news'),
    path('news/<slug:slug>/', news_detail, name='news'),
    path(
         'category/<slug:slug>/',
         NewsByCategory.as_view(extra_context={'title': 'Тайтл'}),
         name='category'
     ),
]
