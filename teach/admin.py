from django.contrib import admin
from .models import TeachFile


@admin.register(TeachFile)
class AdminTeachFile(admin.ModelAdmin):
    list_display = ('title', 'typefile', 'size')
    list_filter = ('typefile', 'size')
