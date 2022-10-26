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

# 1) agregar el urls  OK
# 2) crear la funcion en views.
# 3) crear el template

def paginasumar(request: WSGIRequest):
    numero1 = request.GET.get('numero1',default=0) # recibo el valor
    numero2 = request.GET.get('numero2',default=0)
    total=int(numero1)+int(numero2)
    return render(request,"paginasumar.html",{
        "numero1":numero1,  # envio el valor
        "numero2":numero2,
        "total":total
    })

def paginasumar2(request: WSGIRequest):
    numero1 = request.POST.get('numero1',default=0) # recibo el valor
    numero2 = request.POST.get('numero2',default=0)
    total=int(numero1)+int(numero2)
    return render(request,"paginasumar2.html",{
        "numero1":numero1,  # envio el valor
        "numero2":numero2,
        "total":total
    })