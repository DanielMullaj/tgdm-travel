from django.contrib.auth.models import Permission, User, Group
from django.db import models

# Continent Model
class Continent(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Country Model
class Country(models.Model):
    name = models.CharField(max_length=255)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# City Model
class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Hotel Model
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    standard = models.PositiveIntegerField()
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Airport Model
class Airport(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Trip Model
class Trip(models.Model):
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departures')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrivals')
    to_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    from_airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    departure_date = models.DateField()
    return_date = models.DateField()
    cover = models.ImageField(upload_to='trip_cover', blank=True, null=True)
    number_of_days = models.PositiveIntegerField()
    trailer = models.URLField(blank=True)
    description = models.TextField(blank=True)
    TRIP_TYPE_CHOICES = [
        ('BB', 'Bed & Breakfast'),
        ('HB', 'Half Board'),
        ('FB', 'Full Board'),
        ('AI', 'All Inclusive'),
    ]
    trip_type = models.CharField(max_length=2, choices=TRIP_TYPE_CHOICES)
    price_adult = models.DecimalField(max_digits=10, decimal_places=2)
    price_child = models.DecimalField(max_digits=10, decimal_places=2)
    promoted = models.BooleanField()
    num_places_adult = models.PositiveIntegerField()
    num_places_child = models.PositiveIntegerField()

    def __str__(self):
        return f'Trip from {self.from_city} to {self.to_city}'


# Purchase Model
class Purchase(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    participant_details = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Purchase for {self.trip}'



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField()



