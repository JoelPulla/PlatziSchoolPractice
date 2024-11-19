from django.forms import ModelForm
from .models import Project




class ProjectForm(ModelForm):
    
    class Meta():
        model = Project
        fields = [
            'name', 'description', 'status', 'start_date', 'end_date'
        ]
