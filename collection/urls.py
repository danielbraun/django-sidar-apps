from django.conf.urls import patterns
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

from collection.models import Collectable
from collection.views import CollectableUpdateView, CollectableDeleteView, UpAction, DownAction
from collection.views import SortableCollectableList


urlpatterns = patterns('',
                      (r'^$', login_required(ListView.as_view(model=Collectable)), {}, 'collection-home'),
                      (r'^sort/$', login_required(SortableCollectableList.as_view()), {}, 'collection-sortable-list'),
                       # (r'^(?P<pk>\d+)/$', login_required(UpdateView.as_view(model=Collectable))),
                      (r'^(?P<pk>\d+)/$', login_required(CollectableUpdateView.as_view())),
                      (r'^(?P<pk>\d+)/delete/$', login_required(CollectableDeleteView.as_view())),
                      (r'^(?P<pk>\d+)/up/$', login_required(UpAction.as_view()), {}, "collectable-up"),
                      (r'^(?P<pk>\d+)/down/$', login_required(DownAction.as_view()), {}, "collectable-down"),
                       )
