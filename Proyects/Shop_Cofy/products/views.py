from django.http import HttpResponse
from django.views import generic

from .forms import ProductForm
from django.urls import reverse_lazy

from .models import Product
# Create your views here.


class ProductFromView(generic.FormView):
    # indica el templeate
    template_name = "products/add_product.html"
    # require el formulario
    form_class = ProductForm
    # mensaje de confirmacion 
    success_url = reverse_lazy('all_product')


    #llama a la formulador y accede al meotodo para envair los datos a la BDD
    def form_valid(self, form) :
        form.save()
        return super().form_valid(form)
    
class ProductListView(generic.ListView):
    model = Product
    template_name = "products/all_product.html"
    context_object_name='products'
