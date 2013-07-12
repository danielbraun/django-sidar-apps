# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    user = models.ForeignKey(User, verbose_name=u'מאת משתמש')
    comments = models.TextField(u'תוכן ההערה')

    class Meta:
        verbose_name = u'הערות ממשתמש'
        verbose_name_plural = u'הערות ממשתמשים'

    def __unicode__(self):
        return self.comments
