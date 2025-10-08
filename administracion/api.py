from .models import Usuario
from rest_framework import viewsets, permissions
from .serializers import  EmpresaSerializer, AnunciosSerializer, TipoAnuncioSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permissions_clases = [permissions.AllowAny]
    serializer_class = EmpresaSerializer

class AnunciosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permissions_clases = [permissions.AllowAny]
    serializer_class = AnunciosSerializer

class TipoAnuncioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permissions_clases = [permissions.AllowAny]
    serializer_class = TipoAnuncioSerializer

