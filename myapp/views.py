from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.


def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {'title': title})


def about(request):
    username = 'Quique'
    return render(request, 'about.html', {'username': username})


def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})
    # projects = list(Project.objects.values())
    # return JsonResponse(projects, safe=False)


def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks': tasks})
    # task = Task.objects.get(title=title)
    # return HttpResponse('task: %s'  %task.title)


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {'form': CreateNewTask
                                                          })

    else:
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'], project_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {'form': CreateNewProject})
    else:
    
        Project.objects.create(name = request.POST['name'])
        #print(project)
        #return render(request, 'projects/create_project.html', {'form': CreateNewProject})
        return redirect('projects')

def projects_detail(request, id):
    #projects = Project.objects.get(id=id)
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    #print(projects)
    return render(request, 'projects/detail.html', {'project': project, 'tasks': tasks}) 