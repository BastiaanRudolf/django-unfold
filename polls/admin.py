from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Question, Choice

@admin.register(Question)
class CustomAdminClass(ModelAdmin):
    pass