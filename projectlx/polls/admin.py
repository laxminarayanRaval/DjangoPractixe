from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    # fields = ['choice_text']
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['que_text']}),
        ('Date Information', {'fields': ['pub_date'],
                            'classes': ['collapse']}
        ),
    ]
    list_display = ('que_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    inlines = [ChoiceInline]
    # fields = ['pub_date', 'que_text']

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)