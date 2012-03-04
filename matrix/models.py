# Author: Ziqi Huang, huang.970@osu.edu
# Date: Feb 29, 2012

from django.db import models

class Matrix(models.Model):
    name = models.TextField()
    percent = models.FloatField()
    change = models.FloatField()
    month = models.IntegerField()
    year = models.IntegerField()
