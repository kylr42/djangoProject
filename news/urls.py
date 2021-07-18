from django.urls import path
from news.views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),
    path('news/<int:news_id>/', ViewNews.as_view(), name='news'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
    path(
         'category/<int:category_id>/',
         NewsByCategory.as_view(extra_context={'title': 'Тайтл'}),
         name='category'
     ),
]
