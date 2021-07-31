from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import News, Category, Comment


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = (
        'id', 'title', 'author', 'category', 'created_at',
        'updated_at', 'is_published', 'get_photo',
    )
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category',)
    fields = (
        'title', 'author', 'category', 'content', 'slug', 'photo', 'get_photo',
        'is_published', 'views', 'created_at', 'updated_at',
    )
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('get_photo', 'views', 'created_at', 'updated_at',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75px">')
        return 'Отсутствует'

    get_photo.short_description = 'Фото'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'news', 'created', 'status')
    list_filter = ('status', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'
