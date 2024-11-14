from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse


from .models import Project, Task
from .forms import CreateProjectFrom, CreateTaskForm


# Create your views here.
def index(request):
    return render(request, "index.html")

def projects(request):
    projects = list(Project.objects.values())
    return render(request,"projects.html" , {
        'projects': projects
    })

def tasks(request,):
    task = Task.objects.all()
    return render(request, "tasks.html", {
        "tasks": task
    })
    
def create_Porject(request):
    return render(request, 'create_project.html', {
        'form': CreateProjectFrom
    })

def create_Task(request):
    
    if request.method == 'GET':
        return render(request, 'create_task.html', { 'form':CreateTaskForm })
    else:
        Task.objects.create(title = request.POST['title'], description= request.POST['description'], project_id = 2)
        return redirect('taks/')

def create_task_by_proyect(request, id):
    id_project = Project.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'create_task_by_project.html')
    else:
        Task.objects.create(title = request.POST['title'], description= request.POST['description'], project_id = id_project)
        return redirect('projects')

    
    
    
#este es un jemplo de recibir datos desde el front 
def printData(request, data):
    return HttpResponse(f"Mira el dato que me pasaste es #####{data}####")
