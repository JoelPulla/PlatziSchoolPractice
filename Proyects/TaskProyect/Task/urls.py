
from django.urls import path
from .views import  PrintData, projects, tasks

urlpatterns = [
    path('',projects),
    path('tasks/<int:id>',tasks),
    path('print/<str:data>', PrintData), 
    
]

