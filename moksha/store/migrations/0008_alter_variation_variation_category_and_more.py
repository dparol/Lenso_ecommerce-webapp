# Generated by Django 4.1 on 2022-09-16 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_variation_variation_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('color', 'color'), ('battery', 'battery')], max_length=100),
        ),
        migrations.AlterField(
            model_name='variation',
            name='variation_value',
            field=models.CharField(choices=[('color', 'color'), ('battery', 'battery')], max_length=100),
        ),
    ]
