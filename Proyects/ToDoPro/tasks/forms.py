from django.forms import ModelForm
from .models import Project, Task




class ProjectForm(ModelForm):
    
    class Meta():
        model = Project
        fields = [
            'name', 'description', 'status', 'start_date', 'end_date'
        ]


class TaskForm(ModelForm):
    
    class Meta():
        model = Task
        fields = ['title', 'description', 'limit_date', 'user']