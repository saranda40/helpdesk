from rest_framework import routers
from .api import UsuarioViewSet

router = routers.DefaultRouter()

router.register('api/usuarios',UsuarioViewSet,'usuarios')

urlpatterns = router.urls