# Generated by Django 5.1.6 on 2025-02-14 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='booking',
        ),
        migrations.RemoveField(
            model_name='loyaltypoints',
            name='user',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.RemoveField(
            model_name='review',
            name='vehicle',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='LoyaltyPoints',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
    ]
