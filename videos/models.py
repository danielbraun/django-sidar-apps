# -*- coding: utf-8 -*-
from backoffice.models import Discipline, Category, Designer
from django.db import models


class Video(models.Model):
    video = models.FileField(u'סרטון', upload_to='videos/')
    description = models.CharField(u'תיאור', max_length=255)
    duration = models.PositiveIntegerField(u'משך סרטון')
    year = models.PositiveIntegerField(u'שנה')
    related_designer = models.ForeignKey(Designer,
                                         verbose_name=u'עוסק במעצב',
                                         null=True)
    discipline = models.ForeignKey(Discipline,
                                   verbose_name=Discipline._meta.verbose_name)
    category = models.ForeignKey(Category, null=True,
                                 verbose_name=Category._meta.verbose_name)

    class Meta:
        verbose_name = u'סרטים'
        verbose_name_plural = u'סרטים'

    def __unicode__(self):
        return self.description
