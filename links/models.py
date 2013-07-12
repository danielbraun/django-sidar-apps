from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from backoffice.models import Discipline


class LinkCategory(models.Model):
    name = models.CharField(_('name'), max_length=100)

    class Meta:
        verbose_name = _('Link Category')
        verbose_name_plural = _('Link Categories')

    def __unicode__(self):
        return self.name


class Link(models.Model):
    name = models.CharField(_('site name'), max_length=100)
    url = models.URLField(_('site address'))
    language = models.CharField(_('site language'), max_length=7,
                                choices=map(lambda (k, v): (k, _(v)),
                                            settings.LANGUAGES))
    category = models.ForeignKey('LinkCategory',
                                 verbose_name=_('Link Category'))
    comments = models.CharField(_('comments'), max_length=100, blank=True)
    discipline = models.ForeignKey(Discipline,
                                   verbose_name=_('design discipline'))

    class Meta:
        verbose_name = _('Link')
        verbose_name_plural = _('Links')

    def __unicode__(self):
        return self.name
