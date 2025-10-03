from .generics import generar_crud_api_view

from .serializers import TicketSerializer, AreasSerializer, CargosSerializer, NivelSerializer, AreasSerializer, RespuestaMensajeTicketSerializer, MensajesTicketSerializer, ImagenesSerializer
from .models import Ticket, Areas, Nivel, MensajesTicket, RespuestaMensajeTicket, Cargos, Imagenes


niveles = generar_crud_api_view(
    Modelo=Nivel, 
    Serializer=NivelSerializer, 
    id_key='id', 
    name_key='Nivel'
)

areas = generar_crud_api_view(
    Modelo=Areas, 
    Serializer=AreasSerializer, 
    id_key='id', 
    name_key='Área'
)

cargos = generar_crud_api_view(
    Modelo=Cargos, 
    Serializer=CargosSerializer, 
    id_key='id', 
    name_key='Cargo'
)

imagenes = generar_crud_api_view(
    Modelo=Imagenes, 
    Serializer=ImagenesSerializer, 
    id_key='id', 
    name_key='Imagenes'
)

ticket = generar_crud_api_view(
    Modelo=Ticket, 
    Serializer=TicketSerializer, 
    id_key='id', 
    name_key='Ticket'
)

mensajes = generar_crud_api_view(
    Modelo=MensajesTicket, 
    Serializer=MensajesTicketSerializer, 
    id_key='id', 
    name_key='Mensajes'
)

respuestamensaje = generar_crud_api_view(
    Modelo=RespuestaMensajeTicket, 
    Serializer=RespuestaMensajeTicketSerializer, 
    id_key='id', 
    name_key='Respuestas'
)