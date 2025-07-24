from django.shortcuts import render, redirect
from .models import News, Category


def index(request):

    news = News.objects.all()
    cat = Category.objects.all()
    context = {
        'news': news,
        'cat':cat
    }
    return render(request, 'index2.html', context=context)


def category(request, pk):

    news = News.objects.filter(category_id=pk)
    cat = Category.objects.all()
    context = {
        'news': news,
        'cat':cat
    }
    return render(request, 'category.html', context=context)




