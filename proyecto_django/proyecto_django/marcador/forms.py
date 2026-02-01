from django import forms
from django.contrib.auth.models import User
from .models import Project, Task

class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProjectForm, self).__init__(*args, **kwargs)
        if user:
            # Excluimos al usuario actual de la lista de posibles colaboradores
            self.fields['collaborators'].queryset = User.objects.exclude(id=user.id)

    class Meta:
        model = Project
        fields = ['title', 'description', 'deadline', 'collaborators']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }

class TaskStatusForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status']
