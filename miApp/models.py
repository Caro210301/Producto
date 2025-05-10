from django.db import models  # type: ignore


class Categoria(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self) -> str:
       return self.nombre

class Principal(models.Model):
    Nombre= models.CharField(max_length=50)
    Precio= models.IntegerField()
    categoria= models.ForeignKey(Categoria,on_delete=models.CASCADE)
    Descripcion= models.CharField(max_length=200)
    Stock= models.IntegerField()
    Unidades_Vendidas= models.IntegerField()
    Oferta= models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='', null=True)
    descuento= models.IntegerField(default=0)

    def __str__(self) -> str:
       return self.Nombre
    



   
        
# Create your models here.
