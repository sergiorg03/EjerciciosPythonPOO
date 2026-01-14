from django.contrib import admin
from .models import Project, Task

# Register your models here. 
# Configuración para ver las tareas dentro del detalle del proyecto
class TaskInline(admin.TabularInline):
    model = Task
    extra = 1  # Número de filas vacías para añadir nuevas tareas rápidamente

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # Columnas que se verán en la lista principal de proyectos
    list_display = ('title', 'owner', 'created_at', 'deadline')
    
    # Filtros laterales para navegar mejor
    list_filter = ('owner', 'deadline')
    
    # Buscador por título y descripción
    search_fields = ('title', 'description')
    
    # Incluye las tareas relacionadas para editarlas en la misma pantalla
    inlines = [TaskInline]

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Columnas para la lista de tareas
    list_display = ('title', 'project', 'status', 'priority', 'assigned_to')
    
    # Filtros para encontrar tareas rápidamente por estado o prioridad
    list_filter = ('status', 'priority', 'project')
    
    # Buscador de tareas
    search_fields = ('title', 'description')