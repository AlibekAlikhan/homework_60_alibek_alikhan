from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Article

from webapp.forms import ArticleForm


def product_view(request: WSGIRequest):
    articles = Article.objects.all().order_by("-category")
    context = {
        "articles": articles
    }
    return render(request, "tasks.html", context=context)


def product_create(request: WSGIRequest):
    if request.method == "GET":
        form = ArticleForm()
        return render(request, "product_create.html", context={"form": form})
    form = ArticleForm(data=request.POST)
    if not form.is_valid():
        return render(request, "product_create.html", context={"form": form})
    else:
        article = Article.objects.create(**form.cleaned_data)
        return redirect("detail_view", pk=article.pk)


def detail_view(request: WSGIRequest, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "detail_article.html", context={
        'article': article
    })


def product_update(request: WSGIRequest, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("detail_view", pk=article.pk)
        return render(request, "product_update.html", context={"form": form, article: article})
    form = ArticleForm(instance=article)
    return render(request, "product_update.html", context={"form": form, article: article})


def delete(request: WSGIRequest, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "delete_confirm.html", context={
        'article': article
    })


def deleted_confirm(request: WSGIRequest, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect("index_article")
