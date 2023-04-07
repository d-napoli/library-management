from django.db import models


class Customer(models.Model):
    class CustomerType(models.TextChoices):
        STUDENT = "student"
        TEACHER = "teacher"

    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=40, null=False)
    email = models.CharField(max_length=255, null=False)
    user_type = models.CharField(max_length=7, choices=CustomerType.choices, default=CustomerType.STUDENT)
    is_active = models.BooleanField(default=True, null=False)


class Author(models.Model):
    name = models.CharField(max_length=255, null=False)


class Work(models.Model):
    class TheType(models.TextChoices):
        BOOK = "book"
        NEWSPAPER = "newspaper"
        MAGAZINE = "magazine"

    title = models.CharField(max_length=255, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TheType.choices, default=TheType.BOOK, null=False)


class Exemplary(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)


class Reservation(models.Model):
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    reserved_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    work = models.ForeignKey(Work, on_delete=models.CASCADE, null=True)
