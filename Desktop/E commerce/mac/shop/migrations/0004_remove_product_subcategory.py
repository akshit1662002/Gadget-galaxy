# Generated by Django 4.1.7 on 2023-09-28 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_rename_sub_category_product_subcategory"),
    ]

    operations = [
        migrations.RemoveField(model_name="product", name="subcategory",),
    ]
