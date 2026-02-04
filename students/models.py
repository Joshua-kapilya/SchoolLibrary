from django.db import models

# Create your models here.
from django.db import models
from accounts.models import UserProfile


class Grade(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        limit_choices_to={"role": "student"},
    )

    grade = models.ForeignKey(
        Grade,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    photo = models.ImageField(
        upload_to="students/photos/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.profile.user.get_full_name()
