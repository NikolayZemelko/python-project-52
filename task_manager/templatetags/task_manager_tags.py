from django import template
register = template.Library()


@register.simple_tag
def date_format(datetime, strformat):
    return datetime.strftime(strformat)
