# Generated by Django 5.0.1 on 2024-02-06 06:28

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_checkoutaddress_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutaddress',
            name='country',
            field=django_countries.fields.CountryField(default='US', max_length=2),
        ),
    ]
