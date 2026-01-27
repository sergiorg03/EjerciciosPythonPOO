from django.shortcuts import render
from .models import Project
from django.shortcuts import get_object_or_404, render


# Create your views here.
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/project_detail.html', {
        'project': project
    })