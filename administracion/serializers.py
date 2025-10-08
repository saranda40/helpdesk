# convertir datos de python a json
from rest_framework import serializers
from .models import Empresa, Anuncios, TipoAnuncio
from django.utils import timezone

class EmpresaSerializer(serializers.ModelSerializer):
    usr_modifica = serializers.PrimaryKeyRelatedField(
        queryset=Empresa.objects.all(), 
        required=False, 
        allow_null=True 
    )
    class Meta:
        model = Empresa
        fields = ('id','nombre_empresa','descripcion_empresa','logo','is_activo','logo')
        read_only_fields=('fecha_actualizacion',)
    def update(self, instance, validated_data):
        validated_data['fecha_actualizacion'] = timezone.now()
        return super().update(instance,validated_data)

class TipoAnuncioSerializer(serializers.ModelSerializer):
    usr_modifica = serializers.PrimaryKeyRelatedField(
        queryset=Empresa.objects.all(), 
        required=False, 
        allow_null=True 
    )
    class Meta:
        model = TipoAnuncio
        fields = ('idTipoAnuncio','nombre','descripcion','is_activo')
        read_only_fields=('fecha_actualizacion',) 
    def update(self, instance, validated_data):
        validated_data['fecha_actualizacion'] = timezone.now()
        return super().update(instance,validated_data)

class AnunciosSerializer(serializers.ModelSerializer):
    usr_modifica = serializers.PrimaryKeyRelatedField(
        queryset=Empresa.objects.all(), 
        required=False, 
        allow_null=True 
    )
    class Meta:
        model = Anuncios
        fields = ('id','titulo','contenido','idTipoAnuncio','fecha_creacion','fecha_publicacion','fecha_termino','is_activo')
        read_only_fields=('fecha_creacion',)    
    def update(self, instance, validated_data):
        validated_data['fecha_actualizacion'] = timezone.now()
        return super().update(instance,validated_data)