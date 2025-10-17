# Create your models here.
from django.db import models
from django.conf import settings

class Empresa(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre_empresa = models.CharField(max_length=100)
    descripcion_empresa = models.TextField()
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    is_activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usr_crea = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='empresas_creadas', on_delete=models.CASCADE)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    usr_modifica = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='empresas_modificados', on_delete=models.SET_NULL,null=True,
    blank=True,)

    def __str__(self):
        return self.nombre_empresa

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresa'
        ordering = ['id']

class TipoAnuncio(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=50)
    descripcion =  models.CharField(max_length=50, default='')
    is_activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usr_crea = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tipoanuncio_creadas', on_delete=models.CASCADE)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    usr_modifica = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='tipoanuncio_modificados', on_delete=models.SET_NULL,null=True,
    blank=True,)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'TipoAnuncio'
        verbose_name_plural = 'TipoAnuncios'
        ordering = ['id']

class Anuncios(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    idTipoAnuncio = models.ForeignKey(TipoAnuncio,on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_publicacion = models.DateTimeField(null=True, blank=True)
    fecha_termino = models.DateTimeField(null=True, blank=True)
    is_activo = models.BooleanField(default=True)
    usr_crea = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='anuncios_creadas', on_delete=models.CASCADE)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    usr_modifica = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='anuncios_modificados', on_delete=models.SET_NULL,null=True,
    blank=True,)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Anuncio'
        verbose_name_plural = 'Anuncios'
        ordering = ['id']
