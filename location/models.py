from django.db import models

# Create your models here.
class BinLocation(models.Model):
    loc_lng = models.FloatField()
    loc_lat = models.FloatField()
    building = models.TextField()
    room = models.IntegerField()
