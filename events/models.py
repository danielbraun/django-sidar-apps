# -*- coding: utf-8 -*-
from django.db import models
from tinymce.models import HTMLField


class Event(models.Model):
    title = models.CharField(u'כותרת', max_length=100)
    description = models.CharField(u'תיאור', max_length=100)
    location = models.CharField(u'מיקום', max_length=100)
    date = models.CharField(u'מועד', max_length=100)
    body = HTMLField(u'תוכן')

    class Meta:
        verbose_name = u'אירוע'
        verbose_name_plural = u'אירועים'
