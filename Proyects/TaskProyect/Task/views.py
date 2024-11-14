from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from .models import Project, Task


# Create your views here.
def Index(request):
    return HttpResponse("Index Page")

def PrintData(request, data):
    return HttpResponse(f"Mira el dato que me pasaste es #####{data}####")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse('task: %s' % task.title)