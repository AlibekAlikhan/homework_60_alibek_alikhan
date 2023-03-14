from django.urls import path


from webapp.views.articles import ArticleView, ProductCreateView, ProjectDetailView, ProductUpdateView, ArticleDeleteView

from webapp.views.basket import BasketAddView, BasketView, BasketDeleteView

urlpatterns =[
    path('', ArticleView.as_view(), name="index_article"),
    path('article', ArticleView.as_view(), name="index_article"),
    path('article/create', ProductCreateView.as_view(), name="create_article"),
    path('article/<int:pk>', ProjectDetailView.as_view(), name="detail_view"),
    path('article/<int:pk>/update', ProductUpdateView.as_view(), name="product_update"),
    path('article/<int:pk>/delit', ArticleDeleteView.as_view(), name="article_delit"),
    path('article/<int:pk>/delit/confirm', ArticleDeleteView.as_view(), name="confirm"),
    path('article/<int:pk>/add/basket', BasketAddView.as_view(), name="add_basket"),
    path('article/basket', BasketView.as_view(), name="baskets_view"),
    path('article/basket/<int:pk>', BasketDeleteView.as_view(), name="baskets_delete"),
]