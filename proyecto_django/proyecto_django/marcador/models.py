from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
def validate_not_past(value):
    if value < timezone.now().date():
        raise ValidationError("La fecha límite no puede estar en el pasado.")

class Project (models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Atributo que se actualiza automaticamente cuando se crea el objeto
    deadline = models.DateField(validators=[validate_not_past])
    owner = models.ForeignKey(User, related_name='owned_projects', on_delete=models.CASCADE)  # Relación One-to-Many con el modelo User
    collaborators = models.ManyToManyField(User, related_name='collaborated_projects', blank=True)  # Relación Many-to-Many con el modelo User

    def __str__(self):
        return f"Titulo: {self.title}"
    
class Task(models.Model):
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)  # Relación One-to-Many con el modelo Project
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=[('TODO', 'To Do'), ('IN_PROGRESS', 'In Progress'), ('DONE', 'Done')])  # Opciones: TODO, IN_PROGRESS, DONE
    priority = models.CharField(max_length=100, choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')])  # Opciones: LOW, MEDIUM, HIGH
    #assigned_to = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)  # Relación One-to-Many con el modelo User. Puede ser null si la Tarea (Task) no se ha asignado toadiva a nadie.

    def __str__(self):
        return f"Tarea: {self.title}, ({self.description})"
