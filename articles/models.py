# -*- coding: utf-8 -*-
from django.db import models
from backoffice.models import Designer, Discipline, Category


class Article(models.Model):
    article = models.FileField(upload_to='articles/',
                               verbose_name=u'קובץ המאמר')
    title = models.CharField(u'כותרת', max_length=100)
    category = models.ForeignKey(Category, verbose_name=u'קטגורית עיצוב',
                                 null=True)
    about_designer = models.ForeignKey(Designer, null=True,
                                       verbose_name=u'עוסק במעצב')
    discipline = models.ForeignKey(Discipline, verbose_name=u'תחום עיצוב')

    class Meta:
        verbose_name = u'מאמר'
        verbose_name_plural = 'מאמרים'

    def __unicode__(self):
        return self.title
