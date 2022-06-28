from django import template
import datetime


register = template.Library()


@register.filter(expects_localtime=True)
def is_older_than_a_day(value):
    if isinstance(value, datetime.datetime):
        value = value.date()
    delta = value - datetime.date.today()
    return delta.days > 1