# Importación de las librerias necesarias
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Vista de Dashboard con mis proyectos y colaboraciones
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:project_id>/', views.detail_view, name='detail_view'),
    path('projects/<int:project_id>/delete/', views.delete_project, name='delete_project'),
    path('projects/<int:project_id>/edit/', views.edit_project, name='edit_project'),
    path('tasks/<int:task_id>/edit-status/', views.edit_task_status, name='edit_task_status'),

    # Login / Logout
    path('login/', auth_views.LoginView.as_view(template_name='projects/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]

