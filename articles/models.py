# -*- coding: utf-8 -*-
from django.db import models
from people.models import Person
from backoffice.models import Subject, Category


class Article(models.Model):
    article = models.FileField(upload_to='articles/')
    title = models.CharField(u'כותרת', max_length=100)
    author = models.ForeignKey(Person, verbose_name=u'מחבר',
                               related_name='articles_written')
    about_person = models.ForeignKey(Person, verbose_name=u'מושא',
                                     related_name='articles_about')
    subjects = models.ManyToManyField(Subject, verbose_name=u'נושאים')
    category = models.ForeignKey(Category, verbose_name=u'קטגוריה')
    publish_date = models.DateField(u'תאריך פרסום')
    abstract = models.TextField(u'תקציר')

    class Meta:
        verbose_name = u'מאמר'
        verbose_name_plural = 'מאמרים'

    def __unicode__(self):
        return self.title
