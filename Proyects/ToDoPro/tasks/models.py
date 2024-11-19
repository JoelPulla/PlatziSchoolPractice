from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

status_choices= [
    ('pl', 'Planificacion'),
    ('ed', 'En desarrollo'),
    ('pa', 'En pausa'),
    ('fi', 'Finalizado'),
    ('ca', 'cancelado'),
]

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre", blank=False, null=False)
    description = models.TextField(max_length=500, verbose_name="Descripcion", blank=True, null=True)
    status = models.CharField(max_length=2, choices=status_choices, default='pl')
    start_date = models.DateField(blank=True, null=False, verbose_name="Fecha de inicio")
    end_date = models.DateField(null=True, blank=True, verbose_name="Fecha aproximada de terminacion")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError("La fecha de terminación no puede ser anterior a la fecha de inicio.")
        
    def __str__(self):
        return self.name
    
    
class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nombre", blank=False, null=False)
    description = models.TextField(max_length=500, verbose_name="Descripcion", blank=True, null=True)
    done = models.BooleanField(default=False, null=False, blank=False, verbose_name="Completado")
    limit_date = models.DateField(blank=True, null=True, verbose_name="Fecha limite")
    created_at = models.DateTimeField(auto_now_add=True)
    
    #relations
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuario Asignado")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="proyecto", null=False, blank=False)

    def __str__(self):
        return self.title
