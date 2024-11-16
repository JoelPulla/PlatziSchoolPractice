from django.urls import path

from .views import homeTaks

urlpatterns = [
    path("", homeTaks, name="home_tasks")
]
