from django.db import models

# Create your models here.

class Order(models.Model):
    order_number = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=100)
    date = models.DateField()


class Waypoint(models.Model):
    PICKUP = "Pickup"
    DELIVERY = "Delivery"
    TYPE_CHOICES = [
        (PICKUP, "Pickup"),
        (DELIVERY, "Delivery"),
    ]

    order = models.ForeignKey(Order, related_name="waypoints", on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

