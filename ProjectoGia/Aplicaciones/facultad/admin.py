from django.contrib import admin
from .models import Facultad
# Register your models here.
#admin.site.register(Facultad)

class FacultadAdmin(admin.ModelAdmin):
    #Columnas a mostrarse
    list_display=(
        'id',
        'nombre',
        'nombreCorto',
        'activo'
    )
    #Filtros para ...
    #texto
    search_fields=('nombre',)
    #Lista
    list_filter=('nombreCorto',)


admin.site.register(Facultad,FacultadAdmin)
