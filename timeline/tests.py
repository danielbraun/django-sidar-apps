from django.core.urlresolvers import reverse
from backoffice.models import Discipline
from django.test import TestCase
from .models import Event


class ViewTests(TestCase):
    def setUp(self):
        self.discipline = Discipline.objects.create(name_en="G", active=True)

    def test_event_list(self):
        d2 = Discipline.objects.create(name_en="I", active=True)
        e1 = Event.objects.create(discipline=self.discipline, year=1950,
                                  description='e1')
        e2 = Event.objects.create(year=1968, description='e2')
        e3 = Event.objects.create(discipline=d2, year=2001, description='e3',
                                  type=Event.DISCIPLINE)
        response = self.client.get(
            reverse('timeline_event_list',
                    kwargs={'discipline': self.discipline.id}
                    )
        )
        self.assertIn(e1, response.context['object_list'])
        self.assertIn(e2, response.context['object_list'])
        self.assertNotIn(e3, response.context['object_list'])


class EventTests(TestCase):
    def setUp(self):
        self.d = Discipline.objects.create(name_en="G", active=True)

    def test_get_decade(self):
        e = Event.objects.create(year=1986)
        self.assertEqual(e.get_decade(), 1980)
        e.year = 1800
        self.assertEqual(e.get_decade(), 1870)

    def test_historical_change_from_discipline(self):
        e = Event.objects.create(year=1000, discipline=self.d,
                                 type=Event.DISCIPLINE)
        e.type = e.HISTORICAL
        e.save()
        self.assertEqual(e.discipline, None)
