# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from backoffice.models import Discipline


class Event(models.Model):
    discipline = models.ForeignKey(Discipline, verbose_name=u'תחום עיצוב',
                                   blank=True, null=True)
    year = models.IntegerField(u'שנה')
    description = models.CharField(u'תיאור', max_length=255)

    HISTORICAL = 'HIS'
    DESIGN = 'DES'
    DISCIPLINE = 'DIS'

    TYPE_CHOICES = (
        (HISTORICAL, u'היסטורי'),
        (DESIGN, u'עיצוב'),
        (DISCIPLINE, u'תחום עיצוב'),
    )
    type = models.CharField(u'סוג אירוע', max_length=3, choices=TYPE_CHOICES,
                            default=HISTORICAL)
    is_important = models.BooleanField(u'חשוב?')

    def get_decade(self):
        if self.year < 1880:
            return 1870
        return self.year - self.year % 10

    def save(self, *args, **kwargs):
        if self.type != self.DISCIPLINE:
            self.discipline = None
        return super(Event, self).save(*args, **kwargs)

    def get_absolute_url(self):
        if self.discipline:
            return reverse('timeline_event_list',
                           kwargs={'discipline': self.discipline.id})

    class Meta:
        verbose_name = u'אירוע היסטורי'
        verbose_name_plural = u'אירועים היסטוריים'
        ordering = ('year',)

    def __unicode__(self):
        return self.description
