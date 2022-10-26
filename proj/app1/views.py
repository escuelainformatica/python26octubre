from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.
def pagina1(request):
    return render(request, "pagina1.html",
                  {
                      "num1": 1,
                      "num2": 2,
                      'nombre': 'John Doe'
                      , 'paises': ['chile', 'argentina', 'peru']
                  })


def pagina2(request):
    productos = [
        {"nombre": "cocacola", "cantidad": 10, "precio": 5000},
        {"nombre": "fanta", "cantidad": 22, "precio": 3000},
        {"nombre": "sprite", "cantidad": 33, "precio": 4000},
    ]
    return render(request, "pagina2.html", {"productos":productos})

def paginaform(request: WSGIRequest):
    # http://127.0.0.1:8000/paginaform?nombre=xxxxxxdsdsd&cantidad=333&precio=3330&submit=
    producto={
        "nombre": request.GET.get('nombre'),
        "cantidad": request.GET.get('cantidad'),
        "precio": request.GET.get('precio')
    }
    return render(request,"paginaform.html",{"producto":producto})