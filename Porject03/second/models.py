from django.db import models


# Create your models here.
class Focus(models.Model):
    note_info = models.CharField(max_length=200, null=True, blank=True)
    info_id = models.IntegerField(null=True, blank=True)


class Info(models.Model):
    code = models.CharField(max_length=6)
    short = models.CharField(max_length=10)
    chg = models.CharField(max_length=10)
    turnover = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    highs = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateField(null=True, blank=True)