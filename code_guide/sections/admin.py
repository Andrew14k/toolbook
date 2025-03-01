# sections/admin.py
from django.contrib import admin
from .models import Section, SubSection

# Register the Section and SubSection models
admin.site.register(Section)
admin.site.register(SubSection)
