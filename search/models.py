from django.db import models

# Create your models here.
class Items(models.Model):
    name = models.TextField()
    class_type = models.IntegerField()
    discription = models.TextField()
