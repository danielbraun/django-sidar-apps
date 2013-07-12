# -*- coding: utf-8 -*-

from django import template
register = template.Library()


@register.simple_tag
def hebrew_year(gregorian_year):
    values = {
        1880: u'ר"מ',
        1890: u'ר"נ',
        1900: u'ר"ס',
        1910: u'ר"ע',
        1920: u'ר"פ',
        1930: u'ר"צ',
        1940: u'"ש',
        1950: u'ש"י',
        1960: u'ש"כ',
        1970: u'ש"ל',
        1980: u'ש"מ',
        1990: u'ש"נ',
        2000: u'ש"ס',
        2010: u'ש"ע',
        2020: u'ש"פ',
        2030: u'ש"צ'
    }
    return u'ת' + values[gregorian_year]