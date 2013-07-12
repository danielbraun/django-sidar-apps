from backoffice.views import DisciplineMixin
from django.views.generic.list import ListView
from django.db.models import Q


class EventList(DisciplineMixin, ListView):
    def get_queryset(self):
        return self.model.objects.filter(
            Q(discipline=self.discipline) | Q(discipline=None)
        )
