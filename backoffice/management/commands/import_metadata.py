# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from backoffice.models import Category
from backoffice.sidar_models import Categories
from django.conf import settings
from backoffice.sidar_models import Categoriescategory


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        for db_name in settings.LEGACY_DB_NAMES:
            for category in Categories.objects.using(db_name).all():
                print category.categories_set.all()
