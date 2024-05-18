from django.urls import path
from .views import Registro,cerrar_sesion,loguear
urlpatterns = [
    path('',Registro.as_view(),name="Autenticacion"),
    path('cerrarsesion/',cerrar_sesion,name="CerrarSesion"),
    path('loguear/',loguear,name="Loguear"),
]