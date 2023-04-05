from django.db import models


class CustomerType(models.Model):
    class TheType(models.TextChoices):
        STUDENT = "student"
        TEACHER = "teacher"

    user_type = models.CharField(max_length=7, choices=TheType.choices, default=TheType.STUDENT)

    def __str__(self):
        return f"<ID: {self.pk} - {self.user_type}>"


class Customer(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=40, null=False)
    email = models.CharField(max_length=255, null=False)
    user_type = models.ForeignKey(CustomerType, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, null=False)
