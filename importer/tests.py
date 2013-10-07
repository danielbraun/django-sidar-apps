from django.test import TestCase
from django.contrib.auth.models import User
from backoffice.models import Work
from moderation.models import ModeratedObject
from importer.views import get_physical_path


class FunctionalTests(TestCase):

    def setUp(self):
        User.objects.create_superuser('admin', '', 'admin')
        self.client.login(username='admin', password='admin')
        self.response = self.client.get('/importer/?q=G-KrF-')

    def test_url_existence(self):
        """ A url actually exists so that the app can be accessed """
        self.assertEquals(self.response.status_code, 200)

    def test_filtering(self):
        """ It can filter works based on query """
        self.assertEquals(self.response.context['items'][0]['filename'],
                          "G-KrF-Pos-111.jpg")

    def test_items_are_mounted(self):
        """ Test whether items in design26 are mounted correctly """
        response2 = self.client.get("/importer/design26/models.py")
        self.assertEquals(response2.status_code, 200)

    def test_import_selected_items(self):
        """ Works should be added when I post my selection """
        item_path = self.response.context['items'][0]['full_path']
        self.client.post('/importer/', {'items': [item_path, ]})
        self.assertEquals(ModeratedObject.objects.all().count(), 1)
