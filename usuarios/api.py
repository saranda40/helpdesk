from .models import Usuario
from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permissions_clases = [permissions.AllowAny]
    serializer_class = UsuarioSerializer

    @action(detail=False, methods=['get'], url_path='me')
    def me(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)