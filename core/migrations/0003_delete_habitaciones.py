# Generated by Django 5.0.3 on 2024-08-25 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_habitacion_habitaciones'),
    ]

    operations = [
        migrations.DeleteModel(
            name='habitaciones',
        ),
    ]
