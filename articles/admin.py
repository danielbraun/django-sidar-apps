from django.contrib import admin
from .models import Article
from .filters import ArticleFilterSet


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'about_designer', 'discipline', ]
    list_filter = ArticleFilterSet.Meta.fields

admin.site.register(Article, ArticleAdmin)
