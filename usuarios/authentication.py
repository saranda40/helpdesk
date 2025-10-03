# usuarios/authentication.py

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import Token  # <-- ¡Tu modelo Token!
from django.utils.translation import gettext_lazy as _

class BearerTokenAuthentication(BaseAuthentication):
    """
    Autenticación personalizada usando el esquema 'Bearer'
    y apuntando directamente a nuestro modelo Token personalizado.
    """
    keyword = 'Bearer' # <--- Define explícitamente el prefijo esperado

    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return None # No hay encabezado de Auth, continua sin autenticar

        parts = auth_header.split()

        # 1. Verificar el formato 'Bearer <key>'
        if parts[0] != self.keyword or len(parts) != 2:
            msg = _("Encabezado de autenticación inválido. Debe ser 'Bearer <token>'.")
            raise AuthenticationFailed(msg)

        token_key = parts[1]

        # 2. Búsqueda directa del Token en tu modelo (resuelve el error DoesNotE...)
        try:
            # Token es tu modelo, que SÍ tiene el atributo objects y DoesNotExist
            token = Token.objects.select_related('user').get(key=token_key)
        except Token.DoesNotExist:
            raise AuthenticationFailed(_("Token inválido o expirado."))

        # 3. Devolver el usuario y el token
        return (token.user, token)

    def authenticate_header(self, request):
        return self.keyword