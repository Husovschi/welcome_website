from django.db import models

class Count(models.Model):
    views = models.IntegerField(default=0)
    button_presses = models.IntegerField(default=0)

class Country(models.Model):
    name = models.CharField(max_length=100)
    visits = models.IntegerField(default=0)