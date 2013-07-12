from django.test import TestCase
from .models import Link, LinkCategory
from backoffice.models import Discipline
from django.core.urlresolvers import reverse


def create_link():
    return Link.objects.create(name='Shenkar',
                               url='http://www.shenkar.ac.il',
                               language='he',
                               discipline=Discipline.objects.create(name_en='g', active=True),
                               category=LinkCategory.objects.create(
                               name='Design College'),
                               comments='Shenkar home page'
                               )


class LinkTests(TestCase):
    def setUp(self):
        self.link = create_link()

    def test_link_creation(self):
        """It should be created properly."""
        self.assertEqual(self.link, Link.objects.all()[0])


class ViewTests(TestCase):
    def setUp(self):
        self.link = create_link()

    def test_link_list(self):
        """It should contain the link."""
        response = self.client.get(
            reverse('links_index',
                    kwargs={'discipline': self.link.discipline.id}))
        self.assertIn(self.link, response.context['object_list'])
