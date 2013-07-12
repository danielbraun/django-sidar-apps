# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase

from backoffice.management.commands.import_portfolio import match_is_self_collected, match_collector, match_technique
from backoffice.models import Discipline, Collector, Work
from bibliography.models import BookCategory


class ViewTests(TestCase):

    def assertResponseOK(self, url):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        return response

    def setUp(self):
        self.discipline = Discipline.objects.create(name_en='g', active=True)

    def test_about_page(self):
        self.assertResponseOK('/discipline/%d/about/' % self.discipline.id)

    def test_homepage(self):
        self.assertResponseOK('/')

    def test_discipline_homepage(self):
        self.assertResponseOK('/discipline/%d/' % self.discipline.id)

    def test_book_list(self):
        self.assertResponseOK('/discipline/%d/book/' % self.discipline.id)

    def test_book_list_with_category(self):
        BookCategory(pk=1).save()
        response = self.assertResponseOK('/discipline/%d/book/1/' % self.discipline.id)
        self.assertIn('category', response.context)

    def test_category_list(self):
        self.assertResponseOK('/discipline/%d/category/' % self.discipline.id)

    def test_subject_list(self):
        self.assertResponseOK('/discipline/%d/subject/' % self.discipline.id)

    def test_designer_list(self):
        self.assertResponseOK('/discipline/%d/designer/' % self.discipline.id)

    def test_article_list(self):
        self.assertResponseOK('/discipline/%d/article/' % self.discipline.id)

    def test_video_list(self):
        self.assertResponseOK('/discipline/%d/video/' % self.discipline.id)

    def test_event_list(self):
        self.assertResponseOK('/discipline/%d/event/' % self.discipline.id)

    def test_search_page_loads(self):
        self.assertResponseOK('/discipline/%d/search/' % self.discipline.id)


class ManagementCommandTests(TestCase):
    def test_match_is_self_collected(self):
        self.assertEqual(
            match_is_self_collected(u'ריזינגר דן', u'ריזינגר דן'),
            True)
        self.assertEqual(
            match_is_self_collected(u'גרוס עלי', u'עלי גרוס'),
            True)
        self.assertEqual(
            match_is_self_collected(u'ריזינגר דן', u'מאוסף ריזינגר דן'),
            True)
        self.assertEqual(
            match_is_self_collected(u'האחים שמיר', u'ציונות 2000'),
            False)

    def test_match_collector(self):
        self.assertEqual(
            match_collector(u'האחים שמיר',
                            u'ציונות 2000')[0].name_he, u'ציונות 2000')
        self.assertEqual(match_collector(u'ריזינגר דן', u'ריזינגר דן'), [])

    def test_match_technique(self):
        self.assertEqual(match_technique(u'תלת מימד&#44; קינטיקה'),
                         u'תלת מימד, קינטיקה')


class WorkListViewTests(TestCase):
    def setUp(self):
        self.discipline = Discipline.objects.create(name_en='g', active=True)
        self.collector = Collector.objects.create()
        self.work = Work.objects.create(discipline=self.discipline)
        self.work_with_a_collector = Work.objects.create(discipline=self.discipline)
        self.work_with_a_collector.of_collections.add(self.collector)
        self.collector_response = self.client.get(
            reverse('work-list',
                    kwargs={'discipline': self.discipline.id,
                            'collector': self.collector.id})
        )

    def test_browse_by_collector(self):
        """It should be possible to browse the works a of a collector."""
        self.assertEqual(self.collector_response.status_code, 200)
        self.assertIn(self.work_with_a_collector,
                      self.collector_response.context['object_list'])

    def test_filter_by_collector(self):
        """It should display only the selected collector's works."""
        self.assertNotIn(self.work,
                         self.collector_response.context['object_list'])


class WorkTests(TestCase):

    def test_create_from_photo(self):
        """Creating a work from a photo alone should work properly."""
        # work = Work.create_from_photo(File(open('static/img/G-AdO-Pos-002.jpg')))
        work = Work.create_from_photo('static/img/G-AdO-Pos-002.jpg')
        self.assertEqual(work.discipline.sidar_id, 'G')
        self.assertEqual(work.designer.sidar_id, 'AdO')
        self.assertEqual(work.category.sidar_id, 'Pos')
        self.assertNotEqual(work.raw_image.name, '')

    def test_filename_regex_pattern(self):
        """Work filenames that should be imported"""
        self.assertRegexpMatches('G-AdO-Pos-002.jpg', Work.filename_regex_pattern)
        self.assertRegexpMatches('G-AdO-CV-002b.jpg', Work.filename_regex_pattern)
        self.assertRegexpMatches('G-AdO-Sta-016 copy.jpg', Work.filename_regex_pattern)
        self.assertRegexpMatches('G-AdO-Sta-016 copy 2.jpg', Work.filename_regex_pattern)
