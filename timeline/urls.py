from django.conf.urls import patterns, url

from .models import Event
from timeline.views import EventList


urlpatterns = patterns('',
                       url(r'^$',
                           EventList.as_view(model=Event),
                           name='timeline_event_list')
                       )
