from django.contrib import admin
from miApp.models import Principal

class Registro(admin.ModelAdmin):
    list_display= ['Nombre','Precio','categoria','Descripcion','Stock','Oferta','Unidades_Vendidas','imagen']
    
admin.site.register(Principal,Registro)
# Register your models here.
