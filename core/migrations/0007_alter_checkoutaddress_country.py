# Generated by Django 5.0.1 on 2024-02-06 06:54

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_checkoutaddress_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutaddress',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
