from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Task

# Create your views here.
@login_required
def dashboard(request):
    mis_proyectos = Project.objects.filter(owner=request.user)
    proyectos_colaborativos = Project.objects.filter(collaborators=request.user)

    context = {
        'mis_proyectos': mis_proyectos,
        'proyectos_colaborativos': proyectos_colaborativos
    }

    return render(request, 'projects/projects/dashboard.html', context)

@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    tareas_completadas = []
    for p in projects:
        tareas_completadas.append(Task.objects.filter(project=p, status='DONE').count())

    proyectos_tareas = zip(projects, tareas_completadas)
    return render(request, 'projects/projects/project_list.html', {
        'projects': proyectos_tareas
    })

@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/projects/project_detail.html', {
        'project': project
    })

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    # Verificar si el usuario es el dueño
    if project.owner == request.user:
        project.delete()
    
    return redirect('dashboard')

