# Generated by Django 5.1.6 on 2025-02-14 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rentals', '0002_remove_payment_booking_remove_loyaltypoints_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('pickup_location', models.CharField(max_length=255)),
                ('dropoff_location', models.CharField(max_length=255)),
                ('pickup_date', models.DateField()),
                ('dropoff_date', models.DateField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('booking_status', models.CharField(choices=[('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.AutoField(primary_key=True, serialize=False)),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('vehicle_type', models.CharField(max_length=50)),
                ('fuel_type', models.CharField(max_length=50)),
                ('transmission_type', models.CharField(max_length=50)),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('features', models.TextField()),
                ('availability_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('Credit Card', 'Credit Card'), ('Digital Wallet', 'Digital Wallet')], max_length=50)),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('Pending', 'Pending'), ('Failed', 'Failed')], max_length=50)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.booking')),
            ],
        ),
        migrations.CreateModel(
            name='LoyaltyProgram',
            fields=[
                ('loyalty_id', models.AutoField(primary_key=True, serialize=False)),
                ('points_earned', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.user')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.user'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.user')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.vehicle')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.vehicle'),
        ),
    ]
