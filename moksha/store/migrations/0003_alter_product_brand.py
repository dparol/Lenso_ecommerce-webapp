# Generated by Django 4.1 on 2022-08-31 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
