# Generated by Django 4.2 on 2023-04-12 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0003_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="blog", name="owner",),
    ]