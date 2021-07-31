from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).\
            get_queryset().filter(is_published=True)


class News(models.Model):
    objects = models.Manager()
    published = PublishedManager()
    title = models.CharField(max_length=150, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Url')
    author = models.CharField(max_length=200, verbose_name='Автор')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True, verbose_name='Тег')
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    slug = models.SlugField(unique=True, verbose_name='Url')
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Тег')
    slug = models.SlugField(unique=True, verbose_name='Url')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})
