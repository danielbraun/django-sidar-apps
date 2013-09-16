# -*- coding: utf-8 -*-
import django_filters
from .models import Work, Subject, Collector
from django.db.models import Q


def free(qs, val):
    return Work.objects.filter(
        Q(designer__name_he__icontains=val) |
        Q(designer__name_en__icontains=val) |
        Q(category__name_he__icontains=val) |
        Q(category__name_en__icontains=val) |
        Q(subjects__name_he__icontains=val) |
        Q(name_he__icontains=val)
    )


class WorkFilterSet(django_filters.FilterSet):
    subjects = django_filters.ModelChoiceFilter(
        queryset=Subject.objects.all(),
        label=u'נושא'
    )

    of_collections = django_filters.ModelChoiceFilter(
        queryset=Collector.objects.all(),
        label=u'מאוסף'
    )

    # q = django_filters.CharFilter(
    #     label=u'חיפוש חופשי',
    #    action=free
    # )

    class Meta:
        model = Work
        fields = ['designer', 'of_collections', 'category', 'subjects',
                  'publish_year']
