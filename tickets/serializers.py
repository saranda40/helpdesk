from rest_framework import serializers
from .models import Ticket, Nivel, Areas, Imagenes, Cargos, MensajesTicket, RespuestaMensajeTicket
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone

Usuario = get_user_model() 

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id','titulo','descripcion','fecha_creacion','fecha_cierre','id_nivel','id_area','is_cerrado')
        read_only_fields=('fecha_creacion',)

class NivelSerializer(serializers.ModelSerializer):
    usr_modifica = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(), 
        required=False, 
        allow_null=True 
    )
    class Meta:
        model = Nivel
        fields =('id','nombre','descripcion','is_activo','prioridad','usr_crea','fecha_actualizacion','usr_modifica')
        read_only_fields=('fecha_creacion',)
    def update(self, instance, validated_data):
        validated_data['fecha_actualizacion'] = timezone.now()
        return super().update(instance,validated_data)


class AreasSerializer(serializers.ModelSerializer):
    usr_modifica = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(), 
        required=False, 
        allow_null=True 
    )
    class Meta:
        model = Areas
        fields =('id','nombre','descripcion','is_activo','usr_crea','fecha_actualizacion','usr_modifica')
    def update(self, instance, validated_data):
        validated_data['fecha_actualizacion'] = timezone.now()
        return super().update(instance,validated_data)

class ImagenesSerializer(serializers.ModelSerializer):
    usr_modifica = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(), 
        required=False, 
        allow_null=True 
    )
    class Meta:
        model = Imagenes
        fields =('id','imagen','id_ticket','is_activo')
    def update(self, instance, validated_data):
        validated_data['fecha_actualizacion'] = timezone.now()
        return super().update(instance,validated_data)

class CargosSerializer(serializers.ModelSerializer):
    usr_modifica = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(), 
        required=False, 
        allow_null=True 
    )
    class Meta:
        model = Cargos
        fields =('__all__')
    def update(self, instance, validated_data):
        validated_data['fecha_actualizacion'] = timezone.now()
        return super().update(instance,validated_data)

class MensajesTicketSerializer(serializers.ModelSerializer):
    usr_modifica = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(), 
        required=False, 
        allow_null=True 
    )
    class Meta:
        models = MensajesTicket
        fields =('id_mensaje','id_ticket','mensaje','fecha_visto','fecha_respuesta','is_cerrado','is_activo')
        read_only_fields=('fecha_creacion',) 
    def update(self, instance, validated_data):
        validated_data['fecha_actualizacion'] = timezone.now()
        return super().update(instance,validated_data)

class RespuestaMensajeTicketSerializer(serializers.ModelSerializer):
    usr_modifica = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(), 
        required=False, 
        allow_null=True 
    )
    class Meta:
        models = RespuestaMensajeTicket
        fields=('id_respuesta','id_mensaje','respuesta','is_activo')
        read_only_fields=('fecha_creacion',) 
    def update(self, instance, validated_data):
        validated_data['fecha_actualizacion'] = timezone.now()
        return super().update(instance,validated_data)