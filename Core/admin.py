from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Section, Book, Subject, Topic, Note, Grade, Comprehension


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "section", "author")


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "section")
    list_filter = ("section",)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "subject")
    list_filter = ("subject",)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "topic")
    search_fields = ("title", "content")
    list_filter = ("topic__subject",)

admin.site.register(Grade)
admin.site.register(Comprehension)

