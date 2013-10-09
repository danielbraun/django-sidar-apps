from django.test import TestCase
from django.contrib.auth.models import User
from moderation.models import ModeratedObject
from .models import Item
import sys
from django.conf import settings
import os

TESTING = 'test' in sys.argv
if TESTING:
    settings.PORTFOLIO_CSV_ROOT = os.path.dirname(os.path.realpath(__file__))


class FunctionalTests(TestCase):

    def setUp(self):
        Item.build_database()
        User.objects.create_superuser('admin', '', 'admin')
        self.client.login(username='admin', password='admin')
        self.response = self.client.get('/importer/?q=G-KrF-')

    def test_url_existence(self):
        """ A url actually exists so that the app can be accessed """
        self.assertEquals(self.response.status_code, 200)

    def test_filtering(self):
        """ It can filter works based on query """
        self.assertEquals(self.response.context['items'].count(), 1)

    def test_items_are_mounted(self):
        """ Test whether items in design26 are mounted correctly """
        response2 = self.client.get("/importer/design26/models.py")
        self.assertEquals(response2.status_code, 200)

    def test_import_selected_items(self):
        """ Works should be added when I post my selection """
        item_id = self.response.context['items'][0].id
        self.client.post('/importer/', {'items': [item_id, ]})
        self.assertEquals(ModeratedObject.objects.all().count(), 1)


class ModelTests(TestCase):

    def setUp(self):
        Item.build_database()

    def test_item_exists_in_database(self):
        Item.objects.get(filename="G-KrF-Pos-111.jpg")
