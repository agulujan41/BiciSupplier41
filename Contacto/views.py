from django.shortcuts import render,redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage,send_mail
# Create your views here.

def contacto(request):
    formulario_contacto = FormularioContacto()
    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')
            try:
                send_mail("Mensaje desde BIKESUPPLIER 41", f"El usuario con el nombre {nombre} de email {email} escribe: \n\n {contenido} ",
                    'agulujan41@gmail.com',[email])
                return redirect('/contacto/?valido')
            except:
                  return redirect('/contacto/?novalido')
            
    return render(request,"contacto/contacto.html",{"formcontacto":formulario_contacto})
