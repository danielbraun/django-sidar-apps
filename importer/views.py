# -*- coding: utf-8 -*-

from .models import Item
from django.shortcuts import render
from backoffice.models import Work


def get_files(query):
    if not query:
        return []
    return Item.objects.filter(filename__startswith=query)


def index(request):
    if request.method == "POST":
        for item_id in request.POST.getlist('items'):
            Work.create_from_photo(Item.objects.get(id=item_id).full_path)
    return render(request,
                  "importer/index.html",
                  {'items': get_files(request.GET.get('q'))})
