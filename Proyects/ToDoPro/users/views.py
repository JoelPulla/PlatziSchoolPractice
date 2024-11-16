from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.

class Signup(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    

def logClose(request):
    logout(request)
    return redirect('login')