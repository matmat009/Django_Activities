# Generated by Django 5.1.6 on 2025-02-14 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0007_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='air_conditioning',
        ),
    ]
