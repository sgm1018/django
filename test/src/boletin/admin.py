from django.contrib import admin

# Register your models here.
from .models import Registrado
from .models import Alumno
class AdminRegistrado(admin.ModelAdmin):
    list_display=["__unicode__","nombre","timestamp"]    #CAMPOS QUE SE MOSTRARAN
    list_display_links = ["__unicode__"]                 #DONDE PONER EL LINK PARA ACCEDER
    list_filter=["timestamp","nombre"]                   #FILTROS DE BUSQUEDA
    list_editable = ["nombre"]                              #CAMPOS EDITABLES
    search_fields = ["email", "nombre"]                 #Barra de busqueda
    class Meta:
        model = Registrado
class AdminALumnos(admin.ModelAdmin):
    list_display=["dni","nombre","tlf","email","fechaNacimiento"]
    list_display_links = ["nombre"]
    list_filter=["nombre","fechaNacimiento"]
    search_fields = ["nombre", "email"]   
    class Meta:
        model = Alumno

admin.site.register(Registrado,AdminRegistrado)
admin.site.register(Alumno,AdminALumnos)