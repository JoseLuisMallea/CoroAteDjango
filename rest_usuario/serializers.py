from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from core.models import Usuario

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['idUsuario', 'nombreUsuario', 'correo', 'password']