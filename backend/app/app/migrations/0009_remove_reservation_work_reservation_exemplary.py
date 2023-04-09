# Generated by Django 4.0.1 on 2023-04-09 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_reservation_return_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='work',
        ),
        migrations.AddField(
            model_name='reservation',
            name='exemplary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.exemplary'),
        ),
    ]