from django.contrib import admin
from .models import Category, News

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'title')
    # 'country' Region modelida bo'lishi kerak


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    # misol uchun
    list_filter = ('category',)
