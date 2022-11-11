"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# hola mundo

import app1.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pagina1',app1.views.pagina1),
    path('pagina2',app1.views.pagina2),
    path('paginaform',app1.views.paginaform),
    path('paginasumar',app1.views.paginasumar),
    path('paginasumar2',app1.views.paginasumar2),
    path('ordenes/insertar',app1.views.insertar_orden),
    path('ordenes/listar',app1.views.listar_ordenes),
    path('ordenes/modificar/<int:id>',app1.views.modificar_orden),
    path('ordenes/eliminar/<int:id>',app1.views.eliminar_orden),
]
