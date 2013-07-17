import django_filters
from .models import Article


class ArticleFilterSet(django_filters.FilterSet):
    class Meta:
        model = Article
        fields = ['category', 'about_designer', ]
