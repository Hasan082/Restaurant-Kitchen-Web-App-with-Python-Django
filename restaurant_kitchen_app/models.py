from django.db import models
from django.contrib.auth.models import User


# Create your models here.
meal_types = (
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner'),
    ('dessert', 'Dessert'),
    ('drinks', 'Drinks'),
    ('salads', 'Salads')
)

STATUS = (
    (0, 'Unavailable'),
    (1, 'Available'),
)


class Menu(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    meal_type = models.CharField(choices=meal_types, max_length=255)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.BooleanField(choices=STATUS,default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal