from django.shortcuts import render,redirect
from .carro import Carro
from Tienda.models import Producto


# Create your views here.
def agrega_producto(request,producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agrega(producto=producto)
    return redirect("Tienda")
def elimina_producto(request,producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.elimina(producto=producto)
    return redirect("Tienda")
def resta_producto(request,producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.resta_producto(producto=producto)
    return redirect("Tienda")
def limpia_carro(request,producto_id):
    carro = Carro(request)
    carro.limpia_carro()
    return redirect("Tienda")