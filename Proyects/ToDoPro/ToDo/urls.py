from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from tasks.views import home


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="index"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("users/", include('users.urls'), name='users'),
    path("projects/", include('tasks.urls'), name='in_projects'),
]
