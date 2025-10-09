from django.shortcuts import render

# Create your views here.
from utils.generics import generar_crud_api_view


from .serializers import EmpresaSerializer, AnunciosSerializer, TipoAnuncioSerializer
from .models import Empresa, Anuncios, TipoAnuncio

empresa = generar_crud_api_view(
    Modelo=Empresa, 
    Serializer=EmpresaSerializer, 
    id_key='id', 
    name_key='Empresa'
)

anuncios = generar_crud_api_view(
    Modelo=Anuncios, 
    Serializer=AnunciosSerializer, 
    id_key='id', 
    name_key='Anuncio'
)

tipoanuncio = generar_crud_api_view(
    Modelo=TipoAnuncio, 
    Serializer=TipoAnuncioSerializer, 
    id_key='id', 
    name_key='Tipo Anuncio'
)
