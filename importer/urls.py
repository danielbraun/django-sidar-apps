from django.conf.urls import url, patterns
from django.conf import settings
import sys
import os

TESTING = 'test' in sys.argv
if TESTING:
    settings.PORTFOLIO_CSV_ROOT = os.path.dirname(os.path.realpath(__file__))


urlpatterns = patterns('importer.views',
                       url(regex=r'^$', view='index'),
                       )
urlpatterns += patterns('django.views.static',
                        url(regex=r'^design26/(?P<path>.*)$',
                            view='serve',
                            kwargs={
                                'document_root': settings.PORTFOLIO_CSV_ROOT},
                            name='design26'
                            )
                        )
