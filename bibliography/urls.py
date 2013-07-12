from django.conf.urls import patterns

from bibliography.views import BookListView, BookListViewByCategory


urlpatterns = patterns('',
    (r'^$', BookListView.as_view(), {}, 'book-list'),
    (r'^(\d+)/$', BookListViewByCategory.as_view(), {}, 'book-list'),
)
