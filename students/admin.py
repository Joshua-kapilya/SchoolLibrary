from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserProfile, Grade, Student


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("profile", "grade")
    list_filter = ("grade",)
    search_fields = ("profile__user__username", "profile__user__first_name")
