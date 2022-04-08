from django.contrib import admin

from .models import Choice, Question
admin.site.register([Choice, Question])

# Register your models here.
