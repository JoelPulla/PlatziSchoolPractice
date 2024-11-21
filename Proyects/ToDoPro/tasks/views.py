from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse

from .models import Project, Task
from .forms import ProjectForm, TaskForm


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
    
    
def taks_by_project(id):
    taks = list(Task.objects.filter(project_id = id))
    return taks
    
def detail_project(request, project_id):
    
    project =  get_object_or_404(Project, id = project_id)
    taks = taks_by_project(id=project_id)
    
    return render(request,"app/projects/detail_project.html", {
        'project': project,
        'tasks': taks
    } )
        
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk = project_id)
    project.delete()
    return redirect('home_projects')

def edit_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    
    if request.method == 'GET':
        form = ProjectForm(instance=project)
        return render(request,"app/projects/edit.html", {
            'form': form,
            })
        
    # else:
    #     try:
    #         form = ProjectForm(request.POST, instance=project)
    #         form.save()
    #         return redirect('detail_project', project_id )
    #     except ValueError as error:
    #         return render(request,"app/projects/edit.html", {
    #         'form': form,
    #         'error': f"Error al actualizar la tarea por : {error}"
    #         }) 
        

        
def create_task(request, project_id):
    if request.method == 'GET':
        return render(request,"app/tasks/create_task.html" , {
            'form': TaskForm
        })
    else:
        form = TaskForm(request.POST)
        new_task = form.save(commit=False)
        new_task.project_id = project_id
        new_task.save()
        return redirect('detail_project', project_id)
    
    