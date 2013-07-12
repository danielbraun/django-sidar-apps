from django.conf.urls import patterns, url
from .filters import LinkFilterSet
from backoffice.views import FilterViewByDiscipline


urlpatterns = patterns(
    '',
    url(regex=r'^$',
        view=FilterViewByDiscipline.as_view(filterset_class=LinkFilterSet,
                                            paginate_by=20),
        name='links_index'),
)
