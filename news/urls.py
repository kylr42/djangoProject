from django.urls import path
from django.views.decorators.cache import cache_page

from news.views import *

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('contact/', contact, name='contact'),

    # path('', index, name='home'),
    path('', cache_page(60)(HomeNews.as_view()), name='home'),
    path('news/<int:news_id>/', ViewNews.as_view(), name='news'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
    path(
         'category/<int:category_id>/',
         NewsByCategory.as_view(extra_context={'title': 'Тайтл'}),
         name='category'
     ),
]
