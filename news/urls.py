from django.urls import path
from news.views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:news_id>/', get_news, name='news'),
    path('news/add_news/', add_news, name='add_news'),
]
