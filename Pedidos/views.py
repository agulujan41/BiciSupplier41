from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Carro.carro import Carro
from django.core.mail import send_mail
from .models import Pedido,LineaPedido
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.
@login_required(login_url = "autenticacion/loguear")
def procesador_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id = key,
            cantidad = value['cantidad'],
            user = request.user,
            pedido = pedido
        ))
    enviar_mail(
        pedido = pedido,
        lineas_pedido = lineas_pedido,
        nombreusuario = request.user.username,
        emailusuario = request.user.email
    )
    LineaPedido.objects.bulk_create(lineas_pedido)
    messages.success(request,"El pedido se ha enviado correctamente")
    return redirect("Tienda")

def enviar_mail(**kwargs):
    asunto = "Gracias por el pedido"
    mensaje = render_to_string("email/email.html",{
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreusuario"),
    })
    mensaje_texto = strip_tags(mensaje)
    from_email = "agulujan41@gmail.com"
    to = kwargs.get("emailusuario")

    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)