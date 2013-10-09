from django.conf.urls import url, patterns
from django.conf import settings


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
