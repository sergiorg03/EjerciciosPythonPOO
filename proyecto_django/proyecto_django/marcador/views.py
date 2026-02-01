from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Task
from .forms import ProjectForm, TaskStatusForm
import numpy as np

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
    
    total_tareas = []
    tareas_completadas = []
    for p in projects:
        t = Task.objects.filter(project=p)
        total_tareas.append(t.count())
        tareas_completadas.append(t.filter(status='DONE').count())

    proyectos_tareas = zip(projects, total_tareas, tareas_completadas)
    return render(request, 'projects/projects/project_list.html', {
        'projects': proyectos_tareas
    })

@login_required
def detail_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tareas_completadas = project.tasks.filter(status='DONE').count()
    tareas_pendientes = project.tasks.exclude(status='DONE').count()

    porcentaje_completado = np.round(((tareas_completadas / (tareas_completadas + tareas_pendientes)) * 100), 4)
    
    return render(request, 'projects/projects/detailView.html', {
        'project': project,
        'completadas': tareas_completadas,
        'pendientes': tareas_pendientes,
        'porcentaje_completado': porcentaje_completado,
    })

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    # Verificar si el usuario es el dueño
    if project.owner == request.user:
        project.delete()
    
    return redirect('dashboard')

@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    # Verificar si el usuario es el dueño
    if project.owner != request.user:
        return redirect('detail_view', project_id=project.id)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('detail_view', project_id=project.id)
    else:
        form = ProjectForm(instance=project, user=request.user)
    
    return render(request, 'projects/projects/project_form.html', {
        'form': form,
        'project': project,
        'title': 'Editar Proyecto'
    })

@login_required
def edit_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    project = task.project
    
    # Verificar si el usuario es colaborador
    if request.user not in project.collaborators.all():
        return redirect('detail_view', project_id=project.id)
    
    if request.method == 'POST':
        form = TaskStatusForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('detail_view', project_id=project.id)
    else:
        form = TaskStatusForm(instance=task)
    
    return render(request, 'projects/projects/project_form.html', {
        'form': form,
        'project': project,
        'title': 'Editar Estado de Tarea'
    })
