# Generated by Django 4.0.6 on 2022-10-01 06:13

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=255, null=True, populate_from='product_name', unique=True),
        ),
    ]