# Generated by Django 4.0.1 on 2023-04-09 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_exemplary_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='return_date',
            field=models.DateField(null=True),
        ),
    ]
