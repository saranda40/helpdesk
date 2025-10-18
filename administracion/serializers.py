# convertir datos de python a json
from rest_framework import serializers
from .models import Empresa, Anuncios, TipoAnuncio
from django.utils import timezone
from django.contrib.auth import get_user_model

Usuario = get_user_model() 

class EmpresaSerializer(serializers.ModelSerializer):
    usr_modifica = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(), 
        required=False, 
        allow_null=True 
    )
    class Meta:
        model = Empresa
        fields = ('__all__')
        read_only_fields=('fecha_actualizacion',)
    def update(self, instance, validated_data):
        validated_data['fecha_actualizacion'] = timezone.now()
        return super().update(instance,validated_data)

class TipoAnuncioSerializer(serializers.ModelSerializer):
    usr_modifica = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(), 
        required=False, 
        allow_null=True 
    )
    class Meta:
        model = TipoAnuncio
        fields = ('__all__')
        read_only_fields=('fecha_actualizacion',) 
    def update(self, instance, validated_data):
        validated_data['fecha_actualizacion'] = timezone.now()
        return super().update(instance,validated_data)

class AnunciosSerializer(serializers.ModelSerializer):
    nombre_TipoAnuncio = serializers.CharField(source='IdTipoAnuncio.nombre', read_only=True)
    usr_modifica = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(), 
        required=False, 
        allow_null=True 
    )
    class Meta:
        model = Anuncios
        fields = ('id','titulo','contenido','fecha_publicacion','IdTipoAnuncio','nombre_TipoAnuncio','is_activo','usr_crea','fecha_actualizacion','usr_modifica')
        read_only_fields=('fecha_creacion',)    
    def update(self, instance, validated_data):
        validated_data['fecha_actualizacion'] = timezone.now()
        return super().update(instance,validated_data)