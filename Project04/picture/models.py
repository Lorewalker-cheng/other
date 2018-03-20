from django.db import models


# Create your models here.
class Picture(models.Model):
    name = models.CharField(max_length=20)
    path = models.CharField(max_length=200)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Area(models.Model):
    title = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.title