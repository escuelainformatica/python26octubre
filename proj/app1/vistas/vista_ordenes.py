from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpRequest
from django.shortcuts import render, redirect

from app1.modelos.cliente import Cliente
from app1.modelos.menu import Menu
from app1.modelos.orden import Orden


def insertar_orden(request:HttpRequest):
    boton=request.POST.get('boton','')
    if(boton==""):
        lista_clientes=Cliente.objects.all()
        lista_menus=Menu.objects.all()

        return render(request,'orden/insertar.html',{'lista_clientes':lista_clientes,'lista_menus':lista_menus})
    else:
        cliente=Cliente()
        cliente.id=request.POST.get('cliente',0)

        menu=Menu()
        menu.id=request.POST.get('menu',0)

        nueva_orden=Orden()
        nueva_orden.cliente=cliente
        nueva_orden.menu=menu
        nueva_orden.cantidad=request.POST.get('cantidad',0)
        nueva_orden.save()
        return redirect("/ordenes/listar")

def eliminar_orden(request:HttpRequest,id:int):
    orden = Orden.objects.get(id=id)
    orden.delete()
    return redirect("/ordenes/listar")

def modificar_orden(request:HttpRequest,id:int):
    boton=request.POST.get('boton','')
    if(boton==""):
        lista_clientes=Cliente.objects.all()
        lista_menus=Menu.objects.all()
        orden = Orden.objects.get(id=id)

        return render(request,'orden/modificar.html',{'orden':orden,
                                                      'lista_clientes':lista_clientes,
                                                      'lista_menus':lista_menus})
    else:
        cliente=Cliente()
        cliente.id=request.POST.get('cliente',0)

        menu=Menu()
        menu.id=request.POST.get('menu',0)

        orden_antigua=Orden.objects.get(id=id)
        orden_antigua.cliente=cliente
        orden_antigua.menu=menu
        orden_antigua.cantidad=request.POST.get('cantidad',0)
        orden_antigua.save()
        return redirect("/ordenes/listar")


def listar_ordenes(request:HttpRequest):
    ordenes=Orden.objects.all()

    return render(request,'orden/listar.html',{'ordenes':ordenes})

