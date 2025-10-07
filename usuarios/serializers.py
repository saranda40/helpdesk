# convertir datos de python a json
from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','username','password','first_name','last_name','email','apodo','id_area','id_cargo','date_of_birth','is_active','crea_ticket','is_admin','image_perfil')
        read_only_fields=('date_joined',)
    def create(self, validated_data):
        # 1. Extrae la contraseña antes de pasar el resto de datos
        password = validated_data.pop('password', None)
        
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=password,
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            apodo=validated_data.get('apodo', ''),
            id_area=validated_data.get('id_area'),
            id_cargo=validated_data.get('id_cargo'),
            date_of_birth=validated_data.get('date_of_birth'),
            is_active=validated_data.get('is_active', True),
            crea_ticket=validated_data.get('crea_ticket', True),
            is_admin=validated_data.get('is_admin', False),
            image_perfil=validated_data.get('image_perfil', None)   
        )