#from django.contrib import admin
#
## Register your models here.
#
#from .models import Choice, Question
#
##admin.site.register(Question)
##class QuestionAdmin(admin.ModelAdmin):
##    fields = ['pub_date', 'question_text']
#class QuestionAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['question_text']}),
#        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#    ]
#
#admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)

from django.contrib import admin

from .models import Choice, Question


#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
