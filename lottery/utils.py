from django.db.models import Max
from .models import Prefix
from .models import MiddleTerm
from .models import Suffix
import random


def generate():
        prefix = Prefix.objects.order_by("?").first()
        middle = MiddleTerm.objects.order_by("?").first()
        suffix = Suffix.objects.order_by("?").first()
        if suffix.needs_s == 1:
                insert = "es"
        else:
                insert = "e"
        course_name = prefix.name +  insert + " " + middle.name + suffix.name
        return course_name