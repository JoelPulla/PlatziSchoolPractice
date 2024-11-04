from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Product(models.Model):  # nombre para el cliente final
    name = models.CharField(max_length=150, verbose_name="Nombre")
    descriptions = models.TextField(max_length=300, verbose_name="Descripoción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    url_image= models.URLField(blank=True, null= True, verbose_name="Url de la imagen", )
    avilable = models.BooleanField(default=True, verbose_name="Disponible")
    # Donde se Guardara
    photo = models.ImageField(
        upload_to="logos", null=True, blank=True, verbose_name="Logo del Producto"
    )
    date_create = models.DateTimeField(null=True,verbose_name='Fecha de creacion', auto_now_add=True)

    def __str__(self):
        return self.name 