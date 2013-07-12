# -*- coding: utf-8 -*-
import django_filters
from .models import Work, Subject, Collector


class WorkFilterSet(django_filters.FilterSet):
    subjects = django_filters.ModelChoiceFilter(
        queryset=Subject.objects.all(),
        label=u'נושא'
    )

    of_collections = django_filters.ModelChoiceFilter(
        queryset=Collector.objects.all(),
        label=u'מאוסף'
    )

    class Meta:
        model = Work
        fields = ['designer', 'of_collections', 'category', 'subjects',
                  'publish_year']
