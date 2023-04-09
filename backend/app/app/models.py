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
    work = models.ForeignKey(Work, on_delete=models.CASCADE, null=True, related_name="work_rel")
    is_active = models.BooleanField(default=True)


class Reservation(models.Model):
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    return_date = models.DateField(null=True)
    reserved_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    exemplary = models.ForeignKey(Exemplary, on_delete=models.CASCADE, null=True)
