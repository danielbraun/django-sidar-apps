from django.conf.urls import patterns, url
from feedback.views import MessageCreateView

urlpatterns = patterns('',
                       url(r'send/$', MessageCreateView.as_view(), name="feedback-send")
                       )
