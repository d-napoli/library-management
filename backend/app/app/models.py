from django.db import models


class UserType(models.Model):
    class TheType(models.TextChoices):
        STUDENT = "student"
        TEACHER = "teacher"

    user_type = models.CharField(max_length=7, choices=TheType.choices, default=TheType.STUDENT)
