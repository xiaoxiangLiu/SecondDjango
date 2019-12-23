from django.contrib import admin
from .models import Questions, Choice
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_data', 'question_text']


admin.site.register(Questions, QuestionAdmin)
admin.site.register(Choice)
