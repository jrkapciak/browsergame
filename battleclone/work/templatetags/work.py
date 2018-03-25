from django import template
from datetime import datetime, timedelta, timezone

register = template.Library()


@register.simple_tag
def time_remain(work_object):
    now = datetime.now(timezone.utc)
    work_started = work_object.started
    work_ending = work_started + timedelta(hours=work_object.work_type)
    return str(work_ending - now).split(".")[0] # remove microseconds from string
