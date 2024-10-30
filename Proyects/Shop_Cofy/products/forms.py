from django import forms 

from .models import Product

# you form 
class ProductForm(forms.Form):
    name = forms.CharField(max_length=150, label="Inserta Nombre")
    descriptions = forms.CharField(max_length=300, label="Descripción")
    price =  forms.DecimalField(decimal_places=2,label="Precio", max_digits=10)
    url_image = forms.URLField(label="Url de la imgen", required=False, )
    avilable =  forms.BooleanField(initial=True, label="Disponible")
    photo = forms.ImageField(required=False, label="Foto")
    
    #you save in BDD
    def save(self):
        Product.objects.create(        
            name = self.cleaned_data["name"],
            descriptions =self.cleaned_data["descriptions"],
            price =  self.cleaned_data["price"],
            url_image = self.cleaned_data["url_image"],
            avilable =  self.cleaned_data["avilable"],
            photo = self.cleaned_data["photo"],
        
        )