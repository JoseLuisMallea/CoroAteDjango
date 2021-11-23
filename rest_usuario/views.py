from django.shortcuts import render
from rest_framework import status
from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.serializers import Serializer
from core.models import Usuario
from .serializers import UsuarioSerializers
import json
from django.http.response import JsonResponse
@csrf_exempt
@api_view(['GET', 'POST'])
# Create your views here.

def lista_usuario(request):
    if request.method=='GET':
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializers(usuario, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])

def detalle_usuario(request, correo):
    try:
        usuario = Usuario.objects.get(correo=correo)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer = UsuarioSerializers(usuario)
        return Response(serializer.data)
    if request.method=='PUT':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializers(usuario, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def loginUsuario(request, correo, password):
    try:
        usuario = Usuario.objects.get(correo=correo, password=password)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer = UsuarioSerializers(usuario)
        return Response(serializer.data) 
    else: 
        return Response({"Error": request.data},status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def putUsuario(request, correo):
    jd = json.loads(request.body)
    usuarios = list(Usuario.objects.filter(correo=correo).values())
    if len(usuarios)>0:
        usuario = Usuario.objects.get(correo=correo)
        usuario.correo=jd['correo']
        usuario.password=jd['password']
        usuario.save()
        datos={'message': "success"}
    else:
        datos={'messsage': "Usuario no encontrado"}
    return JsonResponse(datos)

    