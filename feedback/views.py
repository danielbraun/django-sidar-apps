# -*- coding: utf-8 -*-

from django.views.generic.edit import CreateView
from feedback.models import Message
from django.contrib import messages


class MessageCreateView(CreateView):
    model = Message
    success_message = u'ההערות נשלחו בהצלחה, תודה.'

    def form_valid(self, form):
        self.success_url = self.request.GET['next']
        messages.success(self.request, self.success_message,
                         extra_tags='feedback')
        return super(MessageCreateView, self).form_valid(form)
