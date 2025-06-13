from django import template
import markdown
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def markdownify(text):
    return mark_safe(markdown.markdown(text, extensions=['fenced_code', 'codehilite']))