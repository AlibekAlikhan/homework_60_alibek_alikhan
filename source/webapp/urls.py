from django.urls import path

from webapp.views.articles import product_view, product_create, detail_view, category_create, category_view


urlpatterns =[
    path('', product_view, name="index_article"),
    path('article', product_view, name="index_article"),
    path('article/create', product_create, name="create_article"),
    path('article/<int:pk>', detail_view, name="detail_view"),
    path('article/create_category', category_create, name="create_category"),
    path('article/category', category_view, name="category_view")
]