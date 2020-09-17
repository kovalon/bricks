from datetime import datetime

from django.db import models


# Модель Building
from django.db.models import CASCADE


class Building(models.Model):
    address = models.CharField(max_length=255)
    year = models.CharField(max_length=4)

    def __str__(self):
        return "{} building, {} year".format(self.address, self.year)


# Модель Bricks
class Bricks(models.Model):
    building = models.ForeignKey(Building, related_name='bricks', on_delete=CASCADE)
    count = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return "{} bricks for building {}, {} time".format(self.count, self.building, self.date)
