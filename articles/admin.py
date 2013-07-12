from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article']
    list_filter = ['author', 'about_person', 'subjects', 'category',
                   'publish_date']


admin.site.register(Article, ArticleAdmin)
