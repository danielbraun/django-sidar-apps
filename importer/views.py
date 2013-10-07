# TODO: abstract designer directories also
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
import os
from django.conf import settings
from backoffice.models import Work
from django.core.urlresolvers import reverse
import re
import urllib2


def get_full_path(dirpath, filename):
    path = os.path.join(dirpath,
                        filename).replace(settings.PORTFOLIO_CSV_ROOT,
                                          '')
    return reverse('design26',
                   kwargs={'path': path})


def get_physical_path(url):
    return urllib2.unquote(
        url.replace(reverse('design26', kwargs={'path': ''}),
                    settings.PORTFOLIO_CSV_ROOT))


def get_files(query):
    result = []
    if not os.path.exists(settings.PORTFOLIO_CSV_ROOT):
        raise Exception("Could not find PORTFOLIO_CSV_ROOT. Is it mounted?")
    if not query:
        return result

    disciplines = os.listdir(settings.PORTFOLIO_CSV_ROOT)
    for discipline in disciplines:
        wrong_discipline = False
        # Traverse the discipline
        for dirpath, dirnames, filenames in os.walk(
            os.path.join(settings.PORTFOLIO_CSV_ROOT,
                         discipline)):

            for filename in filenames:
                # If it's a valid sidar item, check for if we're in the correct
                # discipline
                filename_matches_regex = re.match(
                    Work.filename_regex_pattern, filename)
                if filename_matches_regex:
                    if query[0] != filename_matches_regex.groups()[0]:
                        wrong_discipline = True
                        break

                    # If it matches the pattern we're searching for, add it
                    if filename.startswith(query):
                        result.append({
                            'filename': filename,
                            'full_path': urllib2.unquote(get_full_path(dirpath,
                                                                       filename))
                        })
            if wrong_discipline:
                wrong_discipline = False
                break
    return result


def index(request):
    if request.method == "GET":
        return render(request,
                      "importer/index.html",
                      {'items': get_files(request.GET.get('q'))})
    if request.method == "POST":
        for item_path_name in request.POST.getlist('items'):
            Work.create_from_photo(get_physical_path(item_path_name))
        return HttpResponse("Success")
