# Generated by Django 4.1 on 2022-09-03 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_old_price'),
        ('category', '0002_alter_categories_options_alter_categories_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]