from django.conf.urls import patterns
from django.conf.urls import url
from backoffice.views import FilterViewByDiscipline
from videos.filters import VideoFilterSet


urlpatterns = patterns(
    '',
    url(regex=r'^$',
        view=FilterViewByDiscipline.as_view(filterset_class=VideoFilterSet,
                                            paginate_by=20),
        name='videos_index'),
)
