from django.urls import path

from .views import *

urlpatterns = [
    path("", projects, name="home_projects"),
    path("create/", ProjectFormView.as_view(), name="create_project"),
    path("<int:project_id>/delete/", delete_project , name="delete_project"),
    path("<int:project_id>/edit/", edit_project , name="edit_project"),
    path("<int:project_id>/",detail_project, name="detail_project"),
    path("<int:project_id>/create_task/",create_task, name="create_taks"),
    path("<int:project_id>/task/<int:task_id>/edit/", done_task, name="done_task"),
    path("<int:project_id>/task/<int:task_id>/delete/", delete_task, name="delete_task")
    
    
    
]
