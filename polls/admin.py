from django.contrib import admin

<<<<<<< HEAD
from .models import Choice, Question, Item
=======
from .models import Choice, Question
>>>>>>> bf2469612169701326422f4adec9b6583fc98eab



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)
<<<<<<< HEAD
admin.site.register(Item)
=======

>>>>>>> bf2469612169701326422f4adec9b6583fc98eab
