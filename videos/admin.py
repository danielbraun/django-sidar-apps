from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ['description', 'related_designer', 'year', 'duration',
                    'category', 'discipline']

admin.site.register(Video, VideoAdmin)
