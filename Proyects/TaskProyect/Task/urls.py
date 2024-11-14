
from django.urls import path
from .views import  printData, projects, tasks, create_Porject, create_Task, create_task_by_proyect

urlpatterns = [
    path("", projects, name="projects"),
    path('tasks/',tasks, name='tasks'),
    path('create/', create_Porject, name='create_project'),
    path('crear_tarea/<int:id>', create_task_by_proyect, name="crear_tarea"),
    
    
    path('create_task/',create_Task, name='create_task'),
    path('print/<str:data>', printData, name='pirntdata'),
]

