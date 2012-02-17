from django.db import models

# Create your models here.
class BinLocation(models.Model):
    loc_lng = models.DecimalField(max_digits = 5, decimal_places = 2)
    loc_lat = models.DecimalField(max_digits = 5, decimal_places = 2)
    building = models.TextField()
    room = models.IntegerField()
