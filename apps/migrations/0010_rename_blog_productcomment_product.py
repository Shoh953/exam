# Generated by Django 4.2 on 2023-04-12 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0009_product_created_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="productcomment", old_name="blog", new_name="product",
        ),
    ]