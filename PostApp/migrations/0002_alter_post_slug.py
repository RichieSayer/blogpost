# Generated by Django 4.2.9 on 2025-01-27 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
