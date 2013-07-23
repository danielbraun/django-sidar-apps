import django_filters
from .models import Video


class VideoFilterSet(django_filters.FilterSet):
    class Meta:
        model = Video
        fields = ['category', ]
