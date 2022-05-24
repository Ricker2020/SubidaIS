from django.contrib import admin
from .models import Estudiante, Habilidades
# Register your models here.
#admin.site.register(Estudiante)
admin.site.register(Habilidades)

class EstudianteAdmin(admin.ModelAdmin):
    #Columnas a mostrarse
    list_display=(
        'id',
        'primernombre',
        'apellido',
        'facultad',
        #agregar una columna
        'full_name'
    )
    def full_name(self, obj):
        return obj.primernombre +' '+obj.apellido
    #Filtros para ...
    #texto
    search_fields=('apellido',)
    #Lista
    list_filter=('facultad',)
    #M2M
    filter_horizontal=('habilidad',)


admin.site.register(Estudiante,EstudianteAdmin)











