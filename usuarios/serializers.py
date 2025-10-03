# convertir datos de python a json
from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','username','password','first_name','last_name','email','apodo','id_area','id_cargo','date_of_birth','is_active','crea_ticket','is_admin','image_perfil')
        read_only_fields=('date_joined',)