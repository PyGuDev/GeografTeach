from django.contrib import admin
from .models import PersonModel, TaskHomeWork, AnswerTaskHomeWork


class AnswerTaskHomeWorkInline(admin.TabularInline):
    model = AnswerTaskHomeWork
    extra = 0


class PersonModelAdmin(admin.ModelAdmin):
    list_display = ["pk", "firstName", "lastName", "classNumber"]
    list_display_links = ["firstName", "lastName"]
    list_filter = ("firstName", "classNumber")
    search_fields = ("firstName", "lastName")

    class Meta:
        model = PersonModel


class TaskHomeWorkAdmin(admin.ModelAdmin):
    list_display = ["pk", "title"]
    list_display_links = ["pk", "title"]
    search_fields = ("title", "pk")
    inline = [AnswerTaskHomeWorkInline]

    class Meta:
        model = TaskHomeWork


class AnswerTaskHomeWorkAdmin(admin.ModelAdmin):
    list_display = ["pk", "task", "estimation"]
    list_display_links = ["pk", "task"]
    search_fields = ("task", "estimation")

    class Meta:
        model = AnswerTaskHomeWork


admin.site.register(PersonModel, PersonModelAdmin)
admin.site.register(TaskHomeWork, TaskHomeWorkAdmin)
admin.site.register(AnswerTaskHomeWork, AnswerTaskHomeWorkAdmin)