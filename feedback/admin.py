from django.contrib import admin
from feedback.models import Message
from django.contrib.admin.options import ModelAdmin

class MessageAdmin(ModelAdmin):
	readonly_fields = list_display = ('user', 'comments')

admin.site.register(Message, MessageAdmin)