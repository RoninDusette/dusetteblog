from django.contrib import admin
from .models import Article, Category


admin.site.register(Article)
admin.site.register(Category)


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}