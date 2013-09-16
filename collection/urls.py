from django.conf.urls import patterns
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

from collection.models import Collectable
from collection import views

urlpatterns = patterns('',
                      (r'^$', login_required(views.collectable_list), {}, 'collection-home'),
                      (r'^sort/$', login_required(views.sortable_collectable_list_view), {}, 'collection-sortable-list'),
                      (r'^slide/$', login_required(views.slideshow_collectable_list_view), {}, 'collection-slideshow-list'),
                      (r'^(?P<pk>\d+)/$', login_required(views.CollectableUpdateView.as_view())),
                      (r'^(?P<pk>\d+)/delete/$', login_required(views.CollectableDeleteView.as_view())),
                      (r'^(?P<pk>\d+)/up/$', login_required(views.UpAction.as_view()), {}, "collectable-up"),
                      (r'^(?P<pk>\d+)/down/$', login_required(views.DownAction.as_view()), {}, "collectable-down"),
                       )
