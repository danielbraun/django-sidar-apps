# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from html2text import html2text

from backoffice.models import Work, Discipline, Designer, Category, Subject
from backoffice.utils import all_portfolio_rows, remove_file_extension, split_languages_from_string
from backoffice.models import Collector
from django.conf import settings
from django.core.files import File
import os

def match_is_self_collected(designer, collector):
    reversed_collector = ' '.join(collector.split()[::-1])
    if designer == collector or designer in collector or reversed_collector == designer:
        return True
    return False


def match_collector(designer, collector):
    if collector and not match_is_self_collected(designer, collector):
        return [Collector.objects.get_or_create(
            name_he=html2text(collector).strip()
        )[0]
        ]
    return []


def match_discipline(row):
    filename = row['Filename']

    if len(filename) < 2 or filename[1] != '-':
        return None
    matched_discipline = None

    for discipline in Discipline.objects.all():
        if discipline.name_en[0] == filename[0]:
            matched_discipline = discipline
    return matched_discipline


def match_country(field):
    tuples = [
        (u'ישראל', 'IL'),
        (u'טוגו', 'TG'),
        (u'מלדיב', 'MV'),
        (u'פולין', 'PL'),
        (u'יורק', 'US'),
        (u'גרמניה', 'DE'),
        (u'איטליה', 'IT'),
        (u'יוגוסלב', 'RS'),
        (u'הברית', 'US'),
        (u'בריטניה', 'UK'),

    ]
    for couple in tuples:
        if couple[0] in field:
            return couple[1]
    return None


def match_technique(technique):
    return html2text(technique).strip()


def match_category(field):
    if field:
        clean_category = split_languages_from_string(field)
        return Category.objects.get_or_create(
            name_he=clean_category['he'],
            defaults={'name_en': clean_category['en']}
        )[0]
    return None


def match_subject(field):
    subjects = []
    if field:
        for subject in html2text(field).split(','):
            if subject.strip():
                subjects.append(
                    (Subject.objects.get_or_create(name_he=subject.strip()))[0]
                )
    return subjects


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        for row in all_portfolio_rows():
            w = Work.objects.create(
                name_he=row.get(u'שם העבודה', ''),
                name_en=row.get('Document Title', ''),
                description_he=html2text(row.get(u'תאור', '')),
                description_en=html2text(row.get(u'Description', '')),
                discipline=match_discipline(row),
                country=match_country(row.get(u'ארץ', '')),
                designer=Designer.objects.get_or_create(
                    name_he=row.get(u'מעצב', ''),
                    defaults={'name_en': row.get('Designer', '')})[0],
                category=match_category(row.get(u'קטגוריה')),
                size_as_text=row.get(u'גודל', ''),
                publish_date_as_text=row.get(u'תאריך', ''),
                publish_year=int(row.get(u'תאריך', ''))if row.get(
                    u'תאריך', '').isdigit() else None,
                client=row.get(u'לקוח', ''),
                technique=match_technique(row.get(u'טכניקה', '')),
                is_self_collected=match_is_self_collected(
                    row.get(u'מעצב', ''),
                    row.get(u'מאוסף', '')),
                raw_image=File(open(os.path.join(
                    settings.PORFOLIO_IMAGE_DIR,
                    row['Filename'])))
            )
            w.subjects = match_subject(row.get(u'נושא'))
            w.of_collections = match_collector(row.get(u'מעצב', ''),
                                               row.get(u'מאוסף', ''))

            for keyword in [keyword.strip() for keyword in html2text(row.get(u'מילות מפתח', '')).split(',')]:
                if keyword:
                    w.tags.add(keyword)
