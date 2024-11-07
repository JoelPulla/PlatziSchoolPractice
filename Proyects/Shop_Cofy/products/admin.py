from django.contrib import admin
from .models import Product

#nos permite visulizar esto en el django admin 
#hereda los atributos de la clase padre
class ProductAdmin(admin.ModelAdmin):
    model = Product
    #muestra estos atributos en la laista del modelo en admin 
    list_display = ['name', 'price']
    # seleccionamos por que atributo puede realizar una busqueda
    search_fields = ['name']

                   #modelo  #clase del registro
                            # nos permite acceder desde el admin 
admin.site.register(Product, ProductAdmin)