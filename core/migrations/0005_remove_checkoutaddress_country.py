# Generated by Django 5.0.1 on 2024-02-06 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_checkoutaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkoutaddress',
            name='country',
        ),
    ]
