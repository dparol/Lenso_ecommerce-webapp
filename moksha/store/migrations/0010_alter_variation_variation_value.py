# Generated by Django 4.1 on 2022-09-19 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_variation_variation_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_value',
            field=models.CharField(choices=[('red', 'red'), ('silver', 'silver'), ('black', 'black'), ('Lb', 'Lb'), ('AA', 'AA')], max_length=100),
        ),
    ]
