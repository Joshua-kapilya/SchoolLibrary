from django.contrib import admin
from .models import Parent

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "profile", "primary_phone")
    search_fields = ("first_name", "last_name", "profile__user__username", "primary_phone")
    list_filter = ("children__grade",)
