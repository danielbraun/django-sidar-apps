from django.conf.urls import patterns, url
from .filters import ArticleFilterSet
from backoffice.views import FilterViewByDiscipline


urlpatterns = patterns(
    '',
    url(regex=r'^$',
        view=FilterViewByDiscipline.as_view(filterset_class=ArticleFilterSet,
                                            paginate_by=20),
        name='article_index'),
)
