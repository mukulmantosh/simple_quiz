from django.contrib import admin
from . import models

admin.site.register(models.TestInformation)
admin.site.register(models.TestDetailedInformation)