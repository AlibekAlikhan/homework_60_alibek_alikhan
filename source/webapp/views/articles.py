from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Article, Category


def product_view(request: WSGIRequest):
    articles = Article.objects.all()
    context = {
        "articles": articles
    }
    return render(request, "tasks.html", context=context)


def category_view(request: WSGIRequest, pk):
    category = get_object_or_404(Category, pk=pk)
    context = {
        "category": category
    }
    return render(request, "categoty.html", context=context)


def product_create(request: WSGIRequest):
    category = Category.objects.all()
    if request.method == "GET":
        context = {
            "category": category
        }
        return render(request, "product_create.html", context=context)
    article_data = {
        "name": request.POST.get('name'),
        "text": request.POST.get('text'),
        "create_at": request.POST.get('create_at'),
        "category": get_object_or_404(Category, pk=int(request.POST.get('category'))),
        "price": request.POST.get('price'),
        "image_url": request.POST.get('image_url')
    }
    article = Article.objects.create(**article_data)
    return redirect("detail_view", pk=article.pk)


def category_create(request: WSGIRequest):
    if request.method == "GET":
        return render(request, "categoty_create.html")
    print(request.POST)
    categoty_data = {
        "status_category": request.POST.get('status_category'),
        "text_category": request.POST.get('text_category'),
    }
    category = Category.objects.create(**categoty_data)
    return redirect("category_view", pk=category.pk)


def detail_view(request: WSGIRequest, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "detail_article.html", context={
        'article': article
    })
