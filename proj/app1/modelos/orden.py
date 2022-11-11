from django.db import models

from app1.modelos.cliente import Cliente
from app1.modelos.menu import Menu


class Orden(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,related_name="cliente")
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="menu")
    cantidad = models.IntegerField(default=0)
