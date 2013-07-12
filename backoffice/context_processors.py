from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.sites.models import Site

from backoffice.models import Discipline


def default(request):
    return {
        'disciplines': Discipline.objects.all(),
        'login_form': AuthenticationForm(),
        'path': request.path,
        'request': request,
        'registration_form': UserCreationForm(),
        'site': Site.objects.get_current()
    }
