import os
import django
import random
from faker import Faker

# 1. Configuración de Django (DEBE ir antes de importar modelos)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

# 2. Ahora sí podemos importar los modelos
from django.contrib.auth.models import User 
from marcador.models import Project, Task

fake = Faker('es_ES')

def create_demo_data(): 
    # 1. Asegurarnos de que hay usuarios con contraseña
    print("Verificando usuarios...")
    if User.objects.count() < 3: 
        print("Creando usuarios de prueba...") 
        for name in ['profe_admin', 'alumno_1', 'alumno_2']: 
            user, created = User.objects.get_or_create(
                username=name, 
                email=f"{name}@ejemplo.com"
            )
            if created:
                user.set_password('admin123')
                user.save()
    
    users = list(User.objects.all())
    if not users:
        print("Error: No hay usuarios disponibles.")
        return

    print(f"Generando proyectos para {len(users)} usuarios...") 
    
    for _ in range(5): 
        owner = random.choice(users) 
        title = fake.catch_phrase()[:250]
        
        project = Project.objects.create(
            title=title, 
            description=fake.paragraph(nb_sentences=3), 
            deadline=fake.date_between(start_date='today', end_date='+60d'), 
            owner=owner 
        ) 
        
        # Añadir colaboradores aleatorios (que no sean el dueño) 
        others = [u for u in users if u != owner] 
        if others:
            num_collaborators = random.randint(1, len(others))
            project.collaborators.set(random.sample(others, k=num_collaborators))

        # 2. Crear Tareas para cada proyecto 
        print(f" -> Añadiendo tareas al proyecto: {project.title}") 
        
        for _ in range(random.randint(3, 7)): 
            Task.objects.create(
                project=project, 
                title=fake.sentence(nb_words=4)[:250].capitalize(), 
                description=fake.sentence(),
                status=random.choice(['TODO', 'IN_PROGRESS', 'DONE']), 
                priority=random.choice(['LOW', 'MEDIUM', 'HIGH']), 
                assigned_to=random.choice(users) 
            ) 

    print("\n--- ¡Base de Datos poblada con éxito! ---")
    print("Tip: Puedes usar la contraseña 'admin123' para los nuevos usuarios.")

if __name__ == '__main__': 
    create_demo_data()
