from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('year', 'description', 'type',
                    'discipline', 'is_important')
    list_filter = ('discipline', 'type', 'is_important')
    actions_on_bottom = True
    actions_on_top = False

admin.site.register(Event, EventAdmin)
