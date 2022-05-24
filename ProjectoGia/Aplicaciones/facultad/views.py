from aiohttp import request
from django.shortcuts import render
from django.views.generic import (ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView)
from .models import Facultad
from Aplicaciones.persona.models import Estudiante
from django.urls import reverse_lazy
# Create your views here.

def facultad(request):
    return render(request, 'facultad/facultad.html')
#Lista de Facultades
class ListarFacultades(ListView):
    model=Facultad
    context_object_name='listaFacultades'
    template_name='facultad/listaFacultades.html'


#Lista para Muchos
class EstFacuView2List(ListView):
    model=Facultad
    context_object_name='listaFacultades'
    template_name='facultad/intentFAC2.html'

#Lista para Muchos
class EstFacuView3List(ListView):
    model=Facultad
    context_object_name='listaFacultades'
    template_name='facultad/intentFAC3.html'


#Lista para Muchos
class EstFacuView4List(ListView):
    model=Facultad
    context_object_name='listaFacultades'
    template_name='facultad/intentFAC4.html'


#Listar Facultades por nombre
class ListarFacuBusqueda(ListView):
    template_name='facultad/facuBusqueda.html'
    context_object_name='facultades'
    model=Estudiante

    def get_queryset(self):
        nombre=self.request.GET.get('nombre','')
        #print('Nombre: ', nombre)
        listResultados=Facultad.objects.filter(nombreCorto=nombre)
        return listResultados

#Listar estudiantes por habilidades
class ListarFacuActiva(ListView):
    template_name='facultad/facuActiva.html'
    model=Estudiante
    context_object_name='facultades'
    def get_queryset(self):
        #estudiante=Estudiante.objects.get(id=2) #Del num Estudiante
        nombre=self.request.GET.get('nombre','')
        #estudiante=Estudiante.objects.get(primernombre=nombre)
        listResultados=Facultad.objects.filter(nombreCorto=nombre)
        return listResultados
#1
class FacuDetailView(DetailView):
    model=Facultad
    template_name='facultad/detailFacu.html'
    
    def get_context_data(self, **kwargs):
       
        context=super(FacuDetailView, self).get_context_data(**kwargs)
        context['titulo']='Facultad'
        return context

#2
class FacuDetailViewAll(TemplateView):
    model=Estudiante
    template_name='facultad/detailFacuAll.html'
    
    def get_context_data(self, **kwargs):
       
        context=super(FacuDetailViewAll, self).get_context_data(**kwargs)
        context['titulo']='Facultad'
        context['base']=Facultad.objects.all()
        return context



#Crear
class SuccessView(TemplateView):
    template_name='facultad/success.html'

class FacultadCreateView(CreateView):
    model=Facultad
    template_name='facultad/crearFacu.html'
    #fields=('__all__')
    fields=['nombre','nombreCorto','activo' ]
    success_url=reverse_lazy('successFacu')



#Delete
class FacultadDeleteView(DeleteView):
    model=Facultad
    template_name='facultad/delete.html'
    success_url=reverse_lazy('success')

#Update
class FacultadUpdateView(UpdateView):
    model=Facultad
    template_name='facultad/crearFacu.html'
    #fields=('__all__')
    fields=['nombre','nombreCorto','activo' ]
    success_url=reverse_lazy('success')

#Update2
class FacultadUpdateView(UpdateView):
    model=Facultad
    template_name='facultad/crearFacu.html'
    #fields=('__all__')
    fields=['nombre','nombreCorto','activo' ]
    success_url=reverse_lazy('success')

#To Update
def idFacultad(request):
    template_name='facultad/idFacu.html'
    idFacu=request.GET.get('id','0')
    print(idFacu)
    return render(request, 'facultad/idFacu.html', {"pk":idFacu }) 


#Actualizar
def intento2(request):
    template_name='facultad/idFacu.html'
    idFacu=request.GET.get('id','2')
    return render(request, 'facultad/crearFacu.html', {"pk":idFacu }) 

