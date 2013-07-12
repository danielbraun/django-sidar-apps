# -*- coding: utf-8 -*-
from django.db import models
from backoffice.models import Work
from django.contrib.auth.models import User
from positions import PositionField


class Collectable(models.Model):
    original_work = models.ForeignKey(Work)
    comments = models.TextField(u'הערות')
    position = PositionField(collection='user', verbose_name=u'מיקום')
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['position']
        verbose_name = u'פריט אוסף'

    def move_up(self):
        self.position -= 1
        self.save()

    def move_down(self):
        self.position += 1
        self.save()
