from django.db.models import Max
from .models import Prefix
from .models import MiddleTerm
from .models import Suffix
from .models import Course
import random


def generate():
        prefix = Prefix.objects.order_by("?").first()
        middle = MiddleTerm.objects.order_by("?").first()
        suffix = Suffix.objects.order_by("?").first()
        pre_name = prefix.name + "e"
        mid_name = middle.name
        suf_name = suffix.name
        if suffix.needs_s == 1:
                pre_name = pre_name + "s"
        if middle.is_own_word == 0:
                suf_name = suf_name.lower()        
        course_name = pre_name + " " + mid_name + suf_name
        return course_name

def add_course(course):
        c = Course(name=course)
        c.save()
        c.id

