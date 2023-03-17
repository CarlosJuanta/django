from django.db import models

# Create your models here.
class Articulos(models.Model):
    codigo= models.IntegerField()
    descripcion= models.CharField(max_length=100)
    precio= models.DecimalField(max_digits=10,decimal_places=2)
    cantidad= models.IntegerField()
    categoria= models.CharField(max_length=100)
    descripcioncat= models.TextField(blank=True)
    