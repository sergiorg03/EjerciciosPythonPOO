# Explicación del Comando de Arranque en Render

Para desplegar tu proyecto en **Render** (o cualquier servidor de producción Linux), se utiliza un servidor de aplicaciones llamado **Gunicorn**. El comando que debes configurar como "Start Command" es:

```bash
gunicorn mysite.wsgi
```

Aquí te explico qué significa cada parte y por qué es necesario:

## 1. ¿Qué es Gunicorn?
Gunicorn (Green Unicorn) es un servidor **WSGI** (Web Server Gateway Interface). 

*   **En desarrollo:** Usas `python manage.py runserver`. Este servidor es solo para pruebas, es lento y no puede manejar muchas conexiones a la vez de forma segura.
*   **En producción:** Usas Gunicorn. Es mucho más rápido, estable y está diseñado para manejar múltiples peticiones de usuarios reales simultáneamente.

## 2. ¿Qué es `mysite.wsgi`?
Este es el "punto de entrada" de tu aplicación de Django. 

*   **`mysite`**: Es el nombre de la carpeta principal de tu proyecto (la que contiene el archivo `settings.py`).
*   **`wsgi`**: Se refiere al archivo `wsgi.py` que Django crea automáticamente dentro de esa carpeta.

Cuando ejecutas `gunicorn mysite.wsgi`, le estás diciendo a Gunicorn: *"Busca la carpeta `mysite`, encuentra el archivo `wsgi.py` y úsalo para arrancar la web"*.

## 3. Configuración en Render
Cuando configures tu **Web Service** en Render, asegúrate de tener estos campos así:

| Campo | Valor |
| :--- | :--- |
| **Runtime** | `Python 3` |
| **Root Directory** | `proyecto_django/proyecto_django` (según tu estructura de carpetas) |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn mysite.wsgi` |

## 4. Notas Importantes
*   **Instalación:** Gunicorn debe estar en tu archivo `requirements.txt` (ya lo hemos añadido en el paso anterior).
*   **Variables de Entorno:** No olvides copiar las variables de tu archivo `.env` (como `SECRET_KEY`, `DB_PASSWORD`, etc.) a la sección **Environment** de Render, ya que el archivo `.env` no se suele subir al servidor por seguridad.
