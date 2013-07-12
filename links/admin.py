from django.contrib import admin
from .models import Link, LinkCategory


class LinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'language', 'category', 'comments',
                    'discipline']
    list_filter = ['language', 'discipline', ]

admin.site.register(Link, LinkAdmin)
admin.site.register(LinkCategory)
