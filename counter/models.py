from django.db import models

class Count(models.Model):
    views = models.IntegerField(default=0)
    button_presses = models.IntegerField(default=0)
