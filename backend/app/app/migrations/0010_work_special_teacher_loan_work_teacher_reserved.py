# Generated by Django 4.0.1 on 2023-04-10 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_reservation_work_reservation_exemplary'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='special_teacher_loan',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='teacher_reserved',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.customer'),
        ),
    ]