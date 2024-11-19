from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse

from .models import Project, Task
from .forms import ProjectForm


# Create your views here.

def home(request):
    return render(
        request,
        "index.html",
    )

def homeProjects(request):
    return render(request, 'app/tasks.html')

def projects(request):
    
    all_taks = list(Task.objects.all())
    total_taks = len(all_taks)
    
    done_task = len(list(Task.objects.filter(done=True)))
    dont_done_taks = len(list(Task.objects.filter(done=False)))
    
    all_projects = list(Project.objects.all())
    total_projects = len(all_projects)
    return render(request, 'app/tasks.html', {
        'all_projects' : all_projects,
        'total_projects': total_projects,
        'taks': all_taks,
        'total_taks' : total_taks,
        'done_task': done_task,
        'dont_done_taks': dont_done_taks
    })    
    
class ProjectFormView(generic.FormView):
    template_name = "app/form_projects.html"
    form_class = ProjectForm
    success_url = reverse_lazy('home_projects')


    #llama a la formulador y accede al meotodo para envair los datos a la BDD
    def form_valid(self, form) :
        form.save()
        return super().form_valid(form)
    
def detail_project(request, project_id):
    
    return render(request,"app/projects/detail_project.html")