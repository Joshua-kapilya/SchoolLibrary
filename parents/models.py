from django.db import models
from accounts.models import UserProfile


class Parent(models.Model):

    profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="parent_profile",
        limit_choices_to={"role": "parent"},
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    photo = models.ImageField(
        upload_to="parents/photos/",
        blank=True,
        null=True
    )

    primary_phone = models.CharField(max_length=20)
    secondary_phone = models.CharField(max_length=20, blank=True)

    address = models.TextField(blank=True)

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
