from django.urls import path

from .views import homeProjects, projects,ProjectFormView, detail_project, create_task, delete_project, edit_project

urlpatterns = [
    path("", projects, name="home_projects"),
    path("create/", ProjectFormView.as_view(), name="create_project"),
    path("<int:project_id>/delete/", delete_project , name="delete_project"),
    path("<int:project_id>/edit/", edit_project , name="edit_project"),
    path("<int:project_id>/",detail_project, name="detail_project"),
    path("<int:project_id>/create_task/",create_task, name="create_taks"),
    
    
]
