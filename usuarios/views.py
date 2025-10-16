from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import IntegrityError # Útil para errores de BD
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import UsuarioSerializer
from .models import Usuario, Token

@api_view(['POST'])
def login(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response({"error": "Faltan credenciales (username/password)."}, status=status.HTTP_400_BAD_REQUEST)

        # 1. Buscar usuario. get_object_or_404 levanta una excepción si no lo encuentra.
        user = get_object_or_404(Usuario, username=username)
        
        # 2. Verificar contraseña
        if not user.check_password(password):
            return Response({"error": "Password Inválida."}, status=status.HTTP_400_BAD_REQUEST)
            
        # 3. Crear/obtener token
        # Nota: Si estás implementando renovación de token, deberías eliminar el viejo aquí
        # Token.objects.filter(user=user).delete() 
        token, created = Token.objects.get_or_create(user=user)
        
        serializer = UsuarioSerializer(instance=user)

        return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)

    except Usuario.DoesNotExist:
        return Response({"error": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        # Captura cualquier otro error (ej. error de base de datos)
        return Response({"error": f"Error inesperado durante el login: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def register(request):
    serializer = UsuarioSerializer(data=request.data)

    if serializer.is_valid():
        try:
            user = serializer.save()
            token = Token.objects.create(user=user) 
            
            response_serializer = UsuarioSerializer(user) 
            
            return Response({"token": token.key, "user": response_serializer.data}, status=status.HTTP_201_CREATED)

        except IntegrityError:
            return Response({"error": "Error de integridad: El usuario ya existe o hay datos duplicados."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": f"Error durante el registro: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PATCH']) 
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user

    if request.method == 'GET':
        serializer = UsuarioSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        try:
            serializer = UsuarioSerializer(user, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"error": f"Error al actualizar el perfil: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    auth_token_object = request.auth
       
    if auth_token_object:
        try:
            auth_token_object.delete()
            return Response(
                {"detail": "Sesión cerrada con éxito. Token eliminado de la base de datos."}, 
                status=status.HTTP_200_OK
            )
        except AttributeError as e:
            return Response(
                {"detail": f"Error de eliminación: El objeto no es un Token válido. ({e})"},
                status=status.HTTP_500_INTERNAL_ERROR
            )
    
    return Response(
        {"detail": "Token no encontrado o autenticación fallida."},
        status=status.HTTP_400_BAD_REQUEST
    )

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)