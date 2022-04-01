from django.db import models
from localflavor.es.forms import ESIdentityCardNumberField, ESPostalCodeField, ESProvinceSelect
# Create your models here.
class Registrado(models.Model):
    nombre = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)

    def __unicode__(self): #python2
        return self.email
    def __str__(self):  #python3
        return self.email


class Alumno(models.Model):
    nombre =models.CharField(max_length=100, blank=True, null=True)
    dni = models.CharField(null=False,max_length=9,default="Ninguno")
    tlf = models.CharField(null=False, max_length=9,default="Ninguno")
    email = models.EmailField(null=False, max_length=100)
    fechaNacimiento = models.DateField(null=False)
    # provincia = ESProvinceSelect()
    # codigoPostal = ESPostalCodeField()
    
    def __unicode__(self):
        return self.dni
    def __str__(self):
        return self.dni