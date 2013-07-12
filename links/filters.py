import django_filters
from .models import Link


class LinkFilterSet(django_filters.FilterSet):
    class Meta:
        model = Link
        fields = ['category', 'language', ]
