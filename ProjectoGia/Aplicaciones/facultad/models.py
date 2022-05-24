from django.db import models

# Create your models here.
class Facultad(models.Model):
    nombre=models.CharField('Nombre', max_length= 50)
    #blank permite empty field
    nombreCorto=models.CharField('NombreCorto', max_length= 10, blank=True, unique=True)
    activo=models.BooleanField('FacultadActiva', default=True)
    
    class Meta:
        #nombre singular
        verbose_name='Facultad'
        #nombre plural
        verbose_name_plural='Facultades'
        ordering=['nombre'] #ordenalos por el nombre
        #Restricciones-no repeticiones

    def __str__(self):
        if self.nombreCorto=='':
            return 'NA'
        else:
            return self.nombre+ ' ('+self.nombreCorto+')'

    def Activa(self):
        
        if self.activo:
            return 'Facultad Activa '
        else:
            return 'Facultad Inactiva '


  