from django.test import TestCase
from backoffice.models import Discipline
from django.core.urlresolvers import reverse
from .models import Article


class ArticleListTests(TestCase):

    def setUp(self):
        self.article = Article.objects.create(
            discipline=Discipline.objects.create(name_en='G', active=True))

    def test_basic_functionality(self):
        """
        It should contain the article.
        """
        response = self.client.get(
            reverse('article_index',
                    kwargs={'discipline': self.article.discipline.id}))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.article, response.context['object_list'])
