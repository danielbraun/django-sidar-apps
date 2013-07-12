from django.core.management.base import BaseCommand
from backoffice.sidar_models import Timeline
import re
from timeline.models import Event
from sidar.settings_common import LEGACY_DB_NAMES
from backoffice.models import Discipline


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        regex = re.compile('(?P<year>\d+) (?P<description>.+)')

        for db_name in LEGACY_DB_NAMES:
            for timeline in Timeline.objects.using(db_name).exclude(description=None):
                for event in timeline.description.split("<br>"):
                    result = regex.match(event)
                    if result:
                        year = result.groupdict()['year']
                        description = result.groupdict()['description'].strip()
                        important = False
                        for term in timeline.description.split(','):
                            if term.strip() in description:
                                important = True
                        Event.objects.get_or_create(discipline=None,
                                                    year=year,
                                                    description=description,
                                                    type=Event.HISTORICAL,
                                                    defaults={'is_important': important}
                                                    )

            for timeline in Timeline.objects.using(db_name).exclude(designers_description=None):
                discipline = Discipline.objects.get(name_en__startswith=db_name[4])
                for event in timeline.designers_description.split("<br>"):
                    result = regex.match(event)
                    if result:
                        year = result.groupdict()['year']
                        description = result.groupdict()['description'].strip()
                        important = False
                        for term in timeline.designers.split(','):
                            if term.strip() in description:
                                important = True
                        Event.objects.get_or_create(year=year,
                                                    description=description,
                                                    type=Event.DISCIPLINE,
                                                    defaults={'discipline': discipline,
                                                              'is_important': important})
