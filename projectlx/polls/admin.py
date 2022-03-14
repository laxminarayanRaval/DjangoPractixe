from django.contrib import admin
from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['que_text']}),
        ('Date Information', {'fields': ['pub_date']})
    ]
    # fields = ['pub_date', 'que_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)