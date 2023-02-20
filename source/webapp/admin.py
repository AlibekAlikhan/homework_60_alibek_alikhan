from django.contrib import admin

from webapp.models import Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "create_at")
    list_filter = ("id", "name", "price", "create_at")
    search_fields = ("name", "text")
    filter = ("text", "name", "price", "category", "create_at")
    readonly_fields = ("id", "create_at")


admin.site.register(Article, ArticleAdmin)
