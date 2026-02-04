from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserProfile, Grade


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("name",)



