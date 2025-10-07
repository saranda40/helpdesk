# usuarios/models.py (Reemplaza las líneas de importación de Token)

from django.db import models
from django.contrib.auth.models import AbstractUser
from tickets.models import Cargos,Areas
from django.conf import settings
from rest_framework.authtoken.models import Token as DRFToken
from django.utils import timezone
from datetime import timedelta

TOKEN_TTL_DAYS = 7

class Token(DRFToken): 
    # Define el campo 'user' (que NO existía en AbstractToken)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        related_name='auth_token',
        on_delete=models.CASCADE,
        verbose_name="User"
    )
    expires_at = models.DateTimeField(null=True, blank=True)
    def save(self, *args, **kwargs):
        # Si el token se está creando por primera vez, o si queremos renovarlo
        if self._state.adding or self.expires_at is None:
            self.expires_at = timezone.now() + timedelta(days=TOKEN_TTL_DAYS)
        
        super().save(*args, **kwargs)

    class Meta:
        # Esto es necesario si estás sobrescribiendo campos del modelo abstracto base
        abstract = False 
        verbose_name = "Token"
        verbose_name_plural = "Tokens"

class Usuario(AbstractUser):
    apodo = models.TextField(max_length=20,null=True,blank=True)
    image_perfil = models.ImageField(upload_to='perfiles/', null=True, blank=True)
    id_area = models.ForeignKey(Areas, on_delete=models.CASCADE,null=True, blank=True)
    id_cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True)
    is_admin = models.BooleanField(default=False, null=True)
    crea_ticket = models.BooleanField(default=False, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usr_crea = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='usr_creados', on_delete=models.CASCADE)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    usr_modifica = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='usr_modificados', on_delete=models.CASCADE)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_set',  # Nombre Único 1
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_permissions_set',  # Nombre Único 2
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    usr_crea = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL,
        null=True,  
        blank=True,
        related_name='usuarios_creados' 
    )

    usr_modifica = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True, 
        blank=True,
        related_name='usuarios_modificados_por' 
    )

    @property
    def es_supervisor(self):
        return bool(self.id_cargo and self.id_cargo.es_supervisor)

    @property
    def is_administrador(self):
        return bool(self.is_admin)

    def __str__(self):
        return f"{self.username} ({self.apodo})"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name} ({self.apodo})"
    
    def get_short_name(self):
        return self.first_name
    
    @property
    def nombre_completo(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def nombre_usuario(self):
        return self.apodo if self.apodo else self.username

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['username']

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['username']

    def create_user(self, password=None, **extra_fields):
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


