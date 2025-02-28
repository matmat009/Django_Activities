from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    vehicle_type = models.CharField(
        max_length=50,
        choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Luxury', 'Luxury')]
    )
    fuel_type = models.CharField(
        max_length=50,
        choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')]
    )
    transmission_type = models.CharField(
        max_length=50,
        choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')]
    )
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField()
    availability_status = models.BooleanField(default=True)
    city = models.CharField(max_length=100)  # Location filter

    def __str__(self):
        return f"{self.make} {self.model} ({self.city})"

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    pickup_date = models.DateField()
    dropoff_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_status = models.CharField(
        max_length=50,
        choices=[('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled'), ('Pending', 'Pending')]
    )

    def __str__(self):
        return f"Booking {self.booking_id} - {self.user.username}"

    def is_vehicle_available(self):
        """Check if the vehicle is available for the given dates."""
        overlapping_bookings = Booking.objects.filter(
            vehicle=self.vehicle,
            pickup_date__lt=self.dropoff_date,
            dropoff_date__gt=self.pickup_date,
            booking_status='Confirmed'
        )
        return not overlapping_bookings.exists()

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(
        max_length=50,
        choices=[('Credit Card', 'Credit Card'), ('Digital Wallet', 'Digital Wallet')]
    )
    payment_status = models.CharField(
        max_length=50,
        choices=[('Success', 'Success'), ('Pending', 'Pending'), ('Failed', 'Failed')]
    )

    def __str__(self):
        return f"Payment {self.payment_id} - {self.payment_status}"

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5)  # Star rating (1-5)
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.user.username} on {self.vehicle.make} {self.vehicle.model}"

class LoyaltyProgram(models.Model):
    loyalty_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points_earned = models.IntegerField(default=0)

    def __str__(self):
        return f"Loyalty {self.loyalty_id} - {self.user.username}"
