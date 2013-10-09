from django.db import models
import os
from django.conf import settings
import re
from backoffice.models import Work
from django.core.urlresolvers import reverse


class Item(models.Model):
    full_path = models.CharField(max_length=200)
    filename = models.CharField(max_length=50)

    def get_filename_url(self):
        path = self.full_path.replace(settings.PORTFOLIO_CSV_ROOT, '')
        return reverse('design26', kwargs={'path': path})

    def is_already_imported(self):
        try:
            Work.objects.get(sidar_id=os.path.splitext(self.filename)[0])
            return True
        except Work.DoesNotExist:
            return False



    @classmethod
    def build_database(cls):
        if not os.path.exists(settings.PORTFOLIO_CSV_ROOT):
            raise Exception(
                "Could not find PORTFOLIO_CSV_ROOT. Is it mounted?")

        for dirpath, dirnames, filenames in os.walk(
                settings.PORTFOLIO_CSV_ROOT):
            for filename in filenames:
                filename_matches_regex = re.match(
                    Work.filename_regex_pattern, filename)
                if filename_matches_regex:
                    Item.objects.create(
                        filename=filename,
                        full_path=os.path.join(dirpath, filename)
                    )
