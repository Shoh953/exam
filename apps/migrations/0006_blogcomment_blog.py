# Generated by Django 4.2 on 2023-04-12 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0005_blogcomment"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogcomment",
            name="blog",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="apps.blog"
            ),
            preserve_default=False,
        ),
    ]
