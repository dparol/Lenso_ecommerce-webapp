# Generated by Django 4.0.6 on 2022-10-01 07:27

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=255, null=True, populate_from='category_name', unique=True),
        ),
    ]
