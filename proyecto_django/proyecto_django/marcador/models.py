from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Project (models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # This field will be set automatically when a new object is created
    deadline = models.DateField()
    owner = models.ForeignKey(User, related_name='owned_projects', on_delete=models.CASCADE)  # One-to-Many relationship with User model
    collaborators = models.ManyToManyField(User, related_name='collaborated_projects', blank=True)  # Many-to-Many relationship with User model

    def __str__(self):
        return f"Titulo: {self.title}"
    
class Task(models.Model):
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)  # One-to-Many relationship with Project model
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=[('TODO', 'To Do'), ('IN_PROGRESS', 'In Progress'), ('DONE', 'Done')])  # Choices: TODO, IN_PROGRESS, DONE
    priority = models.CharField(max_length=100, choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')])  # Choices: LOW, MEDIUM, HIGH
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)  # One-to-Many relationship with User model but can be null if the task is not assigned to anyone yet

    def __str__(self):
        return f"Tarea: {self.title}, ({self.description})"
