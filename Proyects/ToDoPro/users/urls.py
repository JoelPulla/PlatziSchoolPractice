from django.urls import path

from .views import Signup, logClose


urlpatterns = [
    path('logout/', logClose, name='close_session'),
    path('signup/', Signup.as_view(), name="signup"),
    
]
