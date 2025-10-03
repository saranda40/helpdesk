from .models import Usuario
from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permissions_clases = [permissions.AllowAny]
    serializer_class = UsuarioSerializer