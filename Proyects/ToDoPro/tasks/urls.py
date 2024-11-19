from django.urls import path

from .views import homeProjects, projects,ProjectFormView, detail_project

urlpatterns = [
    path("", projects, name="home_projects"),
    path("<int:project_id>/",detail_project, name="detail_project"),
    path("create/", ProjectFormView.as_view(), name="create_project"),
    
]
