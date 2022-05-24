from pyexpat import model
from django.db import models
from Aplicaciones.facultad.models import Facultad
from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):
    habilidad=models.CharField('Habilidad', max_length=50)
    class Meta:
        verbose_name='Habilidad'
        verbose_name_plural='Habilidades de los Estudiantes'
    def __str__(self):
        return self.habilidad

class Estudiante(models.Model):
    tiposEstudiantes=(
        ('0','Nivelación'),
        ('1', 'Pregrado'),
        ('2', 'Maestria'),
        ('3', 'Doctorado')
    )
    primernombre=models.CharField('Nombre', max_length= 50)
    apellido=models.CharField('Apellidos', max_length= 50 )
    nombreCompleto=models.CharField('Nombre Completo', max_length= 100, blank=True )
    tipo=models.CharField('Tipo', max_length= 1, choices=tiposEstudiantes )
    facultad=models.ForeignKey(Facultad, on_delete=models.CASCADE)
    #imagen

    #Carta motivación
    carta=RichTextField()
    #Relación M-M
    habilidad=models.ManyToManyField(Habilidades)

    #Relación muchos a muchos
    
    class Meta:
        #nombre singular
        verbose_name='Estudiante'
        #nombre plural
        verbose_name_plural='Estudiantes matriculados'
        #ordenar por el A; si son iguales por el nombre...
        ordering=[ 'apellido','primernombre']

    def __str__(self):
        hability=""
        for x in self.habilidad.all():
            print(x)
            hability=hability+' | '+str(x) 
    
        return self.primernombre+' '+self.apellido+' | '+self.get_tipo_display()+' | '+self.facultad.nombre+' '+ hability

    def hability(self):
        hability=""
        for x in self.habilidad.all():
            print(x)
            hability=hability+' | '+str(x) 
    
        return hability

    def tipos(self):
        return self.get_tipo_display()


        

