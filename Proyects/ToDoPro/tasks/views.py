from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(
        request,
        "index.html",
    )
    
def homeTaks(request):
    return render(request, 'app/tasks.html')