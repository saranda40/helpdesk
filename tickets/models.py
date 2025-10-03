from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Nivel(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    is_activo = models.BooleanField(default=True)
    prioridad = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usr_crea = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='niveles_creados', on_delete=models.CASCADE)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    usr_modifica = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='niveles_modificados', on_delete=models.CASCADE, null=True,
    blank=True,)

    def __str__(self):
        return self.nombre + ' - ' + str(self.prioridad)

    class Meta:
        verbose_name = 'Nivel'
        verbose_name_plural = 'Niveles'
        ordering = ['id']

class Areas(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    is_activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usr_crea = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='areas_creados', on_delete=models.CASCADE)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    usr_modifica = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='areas_modificados', on_delete=models.CASCADE,null=True,
    blank=True,)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'

class Ticket(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    usr_crea = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='tickets_creados', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField(null=True, blank=True)
    id_nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, null=True, blank=True)
    id_area = models.ForeignKey(Areas, on_delete=models.CASCADE, null=True, blank=True)
    asignado_a = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='assigned_tickets', on_delete=models.CASCADE, null=True, blank=True)
    fecha_asignacion = models.DateTimeField(null=True, blank=True)
    is_cerrado = models.BooleanField(default=False)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    usr_modifica = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='tickes_modificados', on_delete=models.CASCADE,null=True,
    blank=True,)


    def __str__(self):
        return self.titulo + ' - ' + str(self.user.username)
    
    class Meta:
        ordering = ['-fecha_creacion']  # Ordenar por fecha de creación descendente
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'

class Imagenes(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    imagen = models.ImageField(upload_to='imagenes/')
    id_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True, blank=True)
    is_activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usr_crea = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='img_creados', on_delete=models.CASCADE)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    usr_modifica = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='img_modificados', on_delete=models.CASCADE,null=True,
    blank=True,)

    def __str__(self):
        return self.imagen.name + ' - ' + str(self.id_ticket.id) if self.id_ticket else self.imagen.name
    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'
    
class Cargos(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    id_area = models.ForeignKey(Areas, on_delete=models.CASCADE,null=True, blank=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()    
    es_supervisor = models.BooleanField(default=False)
    is_activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usr_crea = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='cargos_creados', on_delete=models.CASCADE)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    usr_modifica = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='cargos_modificados', on_delete=models.CASCADE,null=True,
    blank=True,)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        ordering = ['id']

class MensajesTicket(models.Model):
    id_mensaje = models.AutoField(primary_key=True, auto_created=True)
    id_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True, blank=True)
    mensaje = models.TextField(max_length=200)
    # Usamos related_name para diferenciar los accesos
    fecha_visto = models.DateTimeField(null=True, blank=True)
    fecha_respuesta = models.DateTimeField(null=True, blank=True)
    is_cerrado = models.BooleanField(default=True)
    is_activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usr_crea = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='mensajes_creados', on_delete=models.CASCADE)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    usr_modifica = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='mensajes_modificados', on_delete=models.CASCADE,null=True,
    blank=True,)

    def __str__(self):
        return self.mensaje
    
    class Meta:
        verbose_name = 'Mensajes'
        verbose_name_plural = 'Mensajes'
        ordering = ['id_mensaje']

class RespuestaMensajeTicket(models.Model):
    id_respuesta = models.AutoField(primary_key=True, auto_created=True)
    id_mensaje = models.ForeignKey(MensajesTicket, on_delete=models.CASCADE, null=True, blank=True)
    respuesta = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    is_activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usr_crea = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='respuestas_creados', on_delete=models.CASCADE)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    usr_modifica = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='respuestas_modificados', on_delete=models.CASCADE,null=True,
    blank=True,)

    def __str__(self):
        return self.respuesta

    class Meta:
        verbose_name = 'Respuesta a Mensaje'
        verbose_name_plural = 'Respuestas a Mensajes'
        ordering = ['fecha_creacion']