from django.urls import path
from rest_usuario.views import detalle_usuario, lista_usuario, loginUsuario

urlpatterns = [
    path('lista_usuario', lista_usuario, name="lista_usuario"),
    path('detalle_usuario/<correo>', detalle_usuario, name="detalle_usuario"),
    path('loginUsuario/<correo>/<password>', loginUsuario, name="loginUsuario")
]