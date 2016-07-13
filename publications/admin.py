from django.contrib import admin

from publications.models import Project
from publications.models import Publication

# Register your models here.
admin.site.register(Project)
admin.site.register(Publication)
