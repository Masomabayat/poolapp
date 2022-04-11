from django.contrib import admin

from .models import Choice, Question

admin.site.register(Choice)

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3



class QuestionAdmin(admin.ModelAdmin):
    
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date informations', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

admin.site.register( Question, QuestionAdmin)

# Register your models here.
