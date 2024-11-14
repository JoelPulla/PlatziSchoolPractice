from django import forms

class CreateProjectFrom(forms.Form):
    name = forms.CharField(label="Nombre del Proyecto", max_length=200, required=True)



class CreateTaskForm(forms.Form):
    title = forms.CharField(max_length=100, label="Titulo", required=True)
    description = forms.CharField(widget=forms.Textarea, label="Descripcion")
