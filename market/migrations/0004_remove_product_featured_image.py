# Generated by Django 4.2.16 on 2024-12-03 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_product_category_product_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='featured_image',
        ),
    ]