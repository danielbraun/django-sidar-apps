from backoffice.models import Work
from django import template
register = template.Library()


@register.inclusion_tag('backoffice/work_marquee.html')
def work_marquee(mode='not-inline'):
    context = {'object_list': Work.objects.one_from_each_discipline()}
    if mode == 'inline':
        context['size'] = 135
        context['position'] = "relative"
    else:
        context['size'] = 215
        context['position'] = "absolute"
        context['width'] = 980
    return context
