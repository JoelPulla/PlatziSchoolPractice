from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

def test_view(request, *args, **kwargs): 
    return HttpResponse("Test V iew")



class CarlistView(TemplateView):
    
    template_name = "car_list.html"
    
    def get_context_data(self):
        
        car_list = [
            {"title": "Juana Bnanana"},
            {"Mega": "Pedroe El esacamoso"}    
        ]   
        
        return { 
            "car_list":car_list    
        }


