from django.contrib import admin
from .models import Suffix
from .models import Prefix
from .models import MiddleTerm

# Register your models here.
admin.site.register(Suffix)
admin.site.register(Prefix)
admin.site.register(MiddleTerm)