# convertir datos de python a json
from rest_framework import serializers
from .models import Usuario
from tickets.models import Areas, Cargos

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areas
        fields = ['id', 'nombre']


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargos
        fields = ['id', 'nombre']


class UsuarioSerializer(serializers.ModelSerializer):
    nombre_area = serializers.CharField(source='id_area.nombre', read_only=True)
    nombre_cargo = serializers.CharField(source='id_cargo.nombre', read_only=True)
    class Meta:
        model = Usuario
        fields = [
            'id', 'username', 'email', 'apodo', 'image_perfil',
            'id_area', 'nombre_area', 'id_cargo', 'nombre_cargo',
            'is_active', 'is_admin', 'crea_ticket',
            'date_of_birth', 'fecha_creacion'
        ]
        read_only_fields=('date_joined',)
        extra_kwargs = {
            'password': {'write_only': True} 
        }

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
            date_of_birth=validated_data.get('date_of_birth'),
            is_active=validated_data.get('is_active', True),
            crea_ticket=validated_data.get('crea_ticket', True),
            is_admin=validated_data.get('is_admin', False),
            image_perfil=validated_data.get('image_perfil', None)   
        )
        return user
    

class UserSerializer(serializers.ModelSerializer):
    nombre_area = serializers.CharField(source='id_area.nombre', read_only=True)
    nombre_cargo = serializers.CharField(source='id_cargo.nombre', read_only=True)
    class Meta:
        model = Usuario
        fields = [
            'id',
            'username',
            'email',
            'apodo',
            'image_perfil',
            'id_area',
            'nombre_area',
            'id_cargo',
            'nombre_cargo',
            'is_active',
            'is_admin',
            'crea_ticket',
            'date_of_birth',
            'fecha_creacion'
        ]