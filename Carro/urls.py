from django.urls import path
from .views import *
app_name ="carro"
urlpatterns = [
    path('agrega/<int:producto_id>',agrega_producto,name="Agrega"),
    path('elimina/<int:producto_id>',elimina_producto,name="Elimina"),
    path('resta/<int:producto_id>',resta_producto,name="Resta"),
    path('limpia/',limpia_carro,name="Limpia"),
]