from django.db import models

# Create your models here.
class Usuario(models.Model):
    idUsuario = models.CharField(max_length=5, primary_key=True, verbose_name='Id del usuario')
    nombreUsuario = models.CharField(max_length=50, verbose_name='nombre del usuario')
    correo = models.CharField(max_length=50, verbose_name='Correo del usuario')
    password = models.CharField(max_length=50, verbose_name='contraseña del usuario')

    def __str__(self):
        return self.idUsuario

