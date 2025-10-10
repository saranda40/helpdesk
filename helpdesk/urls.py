"""
URL configuration for helpdesk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from usuarios.views import login, register, profile, logout, MeView
from tickets.views import niveles, areas, cargos, imagenes, mensajes, respuestamensaje
from administracion.views import empresa, anuncios, tipoanuncio
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tickets/',include('tickets.urls')),
    path('api/login/',login),
    path('api/register/',register),
    path('api/profile/',profile),
    path('api/logout/',logout),
    path('api/niveles/',niveles),
    path('api/areas/',areas),
    path('api/cargos/',cargos),
    path('api/imagenes/',imagenes),
    path('api/mensajes/',mensajes),
    path('api/respuestas',respuestamensaje),
    path('api/empresa/',empresa),
    path('api/anuncios/',anuncios),
    path('api/tipoanuncio/',tipoanuncio),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('me/', MeView.as_view(), name='user-me'),
    path('api/user/', include('users.urls')),

]
