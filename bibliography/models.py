# -*- coding: utf-8 -*-

from django.db import models
from backoffice.models import Discipline


class BookCategory(models.Model):
    name = models.CharField(u'שם הספר', max_length=128)

    class Meta:
        verbose_name = u'קטגורית ספר'
        verbose_name_plural = u'קטגוריות ספרים'
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Book(models.Model):
    author_as_text = models.CharField(u'מחבר/עורך/מאייר', max_length=256)
    title = models.CharField(u'כותרת', max_length=256)
    publication_as_text = models.CharField(u'הוצאה/מקום/שנה', max_length=256)
    category = models.ForeignKey(BookCategory, verbose_name=u'קטגוריה')
    discipline = models.ForeignKey(Discipline, verbose_name=u'תחום עיצוב')
    comments = models.CharField(u'הערות', max_length=256)

    class Meta:
        verbose_name = u'ספר'
        verbose_name_plural = u'ספרים'
        ordering = ['author_as_text', ]

    def __unicode__(self):
        return self.title
