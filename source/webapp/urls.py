from django.urls import path

from webapp.views.articles import product_view, product_create, detail_view, product_update, delete, deleted_confirm


urlpatterns =[
    path('', product_view, name="index_article"),
    path('article', product_view, name="index_article"),
    path('article/create', product_create, name="create_article"),
    path('article/<int:pk>', detail_view, name="detail_view"),
    path('article/<int:pk>/update', product_update, name="product_update"),
    path('article/<int:pk>/delit', delete, name="article_delit"),
    path('article/<int:pk>/delit/confirm', deleted_confirm, name="confirm")
]