from django.db import models


class Menu(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField(default=0)
