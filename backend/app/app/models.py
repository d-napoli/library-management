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


class Exemplary(models.Model):
    class TheType(models.TextChoices):
        BOOK = "book"
        NEWSPAPER = "newspaper"
        MAGAZINE = "magazine"

    title = models.CharField(max_length=255, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    exemplary_type = models.CharField(max_length=10, choices=TheType.choices, default=TheType.BOOK, null=False)


class ExemplaryAvailables(models.Model):
    exemplary = models.ForeignKey(Exemplary, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class Reservation(models.Model):
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    reserved_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    exemplary = models.ForeignKey(Exemplary, on_delete=models.CASCADE)
