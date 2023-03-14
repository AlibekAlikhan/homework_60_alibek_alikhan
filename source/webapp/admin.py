from django.contrib import admin

from webapp.models.article import Article

from webapp.models import Order

from webapp.models import Products


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "create_at")
    list_filter = ("id", "name", "price", "create_at")
    search_fields = ("name", "text")
    filter = ("text", "name", "price", "category", "create_at")
    readonly_fields = ("id", "create_at")


class OrderAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    filter = ["name"]
    readonly_fields = ["id"]

class ProductsAdmin(admin.ModelAdmin):
    search_fields = ["count"]
    filter = ["count"]
    readonly_fields = ["id"]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Products, ProductsAdmin)
