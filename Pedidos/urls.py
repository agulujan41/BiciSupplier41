from django.urls import path
from .views import procesador_pedido

urlpatterns = [
    path('',procesador_pedido,name="Pedido"),
    
]