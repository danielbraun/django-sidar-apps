from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from collection.models import Collectable


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('john',
                                             'lennon@thebeatles.com',
                                             'johnpassword')
        self.client.login(username="john", password="johnpassword")

    def assertResponseOK(self, url):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        return response

    def test_collection_home(self):
        self.assertResponseOK(reverse('collection-home'))

    def test_up_action(self):
        c1 = Collectable.objects.create(original_work_id=1, user=self.user)
        c2 = Collectable.objects.create(original_work_id=1, user=self.user)
        response = self.client.post(reverse('collectable-up',
                                            kwargs={'pk': c2.id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Collectable.objects.get(pk=c2.id).position, 0)
        self.assertEqual(Collectable.objects.get(pk=c1.id).position, 1)

    def test_down_action(self):
        c1 = Collectable.objects.create(original_work_id=1, user=self.user)
        c2 = Collectable.objects.create(original_work_id=1, user=self.user)
        response = self.client.post(reverse('collectable-down',
                                            kwargs={'pk': c1.id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Collectable.objects.get(pk=c2.id).position, 0)
        self.assertEqual(Collectable.objects.get(pk=c1.id).position, 1)
