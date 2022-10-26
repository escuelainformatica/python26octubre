# python26octubre

## crear proyecto

```shell
echo crear carpeta
cd c:\pythoncurso
mkdir oct26b
cd oct26b
echo cree ambiente virtual y lo active
python -m venv venv
cd venv
cd scripts
activate
echo instale django
cd ..
cd ..
py -m pip install Django
echo cree el proyecto
django-admin startproject proj
echo cree la aplicacion
cd proj
python .\manage.py startapp app1 
```

## abrir en Pycharm

Seleccione la carpeta de proj, y con el boton derecho la marque como "source root"

## editar la configuracion

en proj->proj->settings editar lo siguiente: (linea DIRS)

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

y tambien cambiar lo siguiente: (agregar la aplicacion a INSTALLED_APPS)

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app1'
]
```

## crear la carpeta templates

En la raiz de proj, crear la carpeta "templates".

## Crear un ejemplo.

### Editar la urls

en proj/urls.py agregar lo siguiente: (agregar la funcion de la vista)

```python
import app1.views # agregar esto

urlpatterns = [
    path('admin/', admin.site.urls),  # <-- no olvide la coma al final
    path('pagina1',app1.views.pagina1) # y agregar esto 
]
```

### Editar la view

En el archivo app1/views.py editar lo siguiente:

```python
from django.shortcuts import render

def pagina1(request):
    return render(request,"pagina1.html",{})
```

### editar el template

En la carpeta de template, crear un archivo pagina1.html e ingresar dentro del body lo siguiente.

```html
<h1>hola mundo</h1>
```

### Correr el proyecto

En pycharm, abrir el terminal y ejecutar lo siguiente

```shell
python .\manage.py runserver 
```