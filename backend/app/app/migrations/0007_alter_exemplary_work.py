# Generated by Django 4.0.1 on 2023-04-08 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_work_remove_exemplary_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exemplary',
            name='work',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_rel', to='app.work'),
        ),
    ]
