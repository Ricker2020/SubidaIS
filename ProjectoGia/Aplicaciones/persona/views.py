from asyncio.windows_events import NULL
from multiprocessing import context
from re import template
from attr import field
from django.shortcuts import render
from django.views.generic import (ListView, DetailView, TemplateView, 
CreateView, UpdateView, DeleteView)
from .models import Estudiante
from django.urls import reverse_lazy
from Aplicaciones.facultad.models import Facultad
# Create your views here.

def estudiantes(request):
    return render(request, 'persona/estudiante.html')




def intento1(request):
    template_name='persona/idEst1.html'
    nombre=request.GET.get('id','')
    return render(request, 'persona/idEst2.html', {"variable":nombre }) #Usa ruta y diccionario

class intento2(TemplateView):
    model=Estudiante
    template_name='persona/idEst1.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        nombre=self.request.GET.get('id','')
        return render(self, 'persona/idEst2.html', {"variable":nombre })



class ListarFacultades(ListView):
    model=Facultad
    context_object_name='listaFacultades'
    template_name='persona/intentFAC.html'


def facuEstudiantes(request):
    return render(request, 'persona/facuEstudiantes.html')

def idEstudiante(request):
    return render(request, 'persona/idEstudiante.html')

#Lista de Estudiante
class ListarEstudiantes(ListView):
    model=Estudiante
    context_object_name='listaEstudiantes'
    template_name='persona/listaEstudiantes.html'

#Listar estudiantes por facultad
class ListarEstFacu(ListView):
    model=Estudiante
    template_name='persona/listEstFacu.html'
    #tomar nombre
    def get_queryset(self): #sobreescrita
        #Recoger desde el get
        facultadBusqueda=self.kwargs['facultad'] #mismo nombre que en la url
        print(facultadBusqueda)
        #Comparar Atributo de tablas diferentes F<->E
        listResult=Estudiante.objects.filter(facultad__nombreCorto=facultadBusqueda)
        print(listResult)
        return listResult

#Listar estudiantes por facultad 2
class ListarEstFacu2(ListView):
    model=Estudiante
    template_name='persona/listEstFacu2.html'
    #tomar nombre
    def get_queryset(self): #sobreescrita
        #Recoger desde el get
        facultadBusqueda=self.kwargs['facultad'] #mismo nombre que en la url
        print(facultadBusqueda)
        #Comparar Atributo de tablas diferentes F<->E
        listResult=Estudiante.objects.filter(facultad__nombreCorto=facultadBusqueda)
        print(listResult)
        return listResult
#Listar estudiantes por facultad 3
class ListarEstFacu3(ListView):
    model=Estudiante
    template_name='persona/listEstFacu3.html'
    #tomar nombre
    def get_queryset(self): #sobreescrita
        #Recoger desde el get
        facultadBusqueda=self.kwargs['facultad'] #mismo nombre que en la url
        print(facultadBusqueda)
        #Comparar Atributo de tablas diferentes F<->E
        listResult=Estudiante.objects.filter(facultad__nombreCorto=facultadBusqueda)
        print(listResult)
        return listResult

#Listar estudiantes por facultad 4
class ListarEstFacu4(ListView):
    model=Estudiante
    template_name='persona/listEstFacu4.html'
    #tomar nombre
    def get_queryset(self): #sobreescrita
        #Recoger desde el get
        facultadBusqueda=self.kwargs['facultad'] #mismo nombre que en la url
        print(facultadBusqueda)
        #Comparar Atributo de tablas diferentes F<->E
        listResult=Estudiante.objects.filter(facultad__nombreCorto=facultadBusqueda)
        print(listResult)
        return listResult

#Listar estudiantes por nombre(pasado por get) 
#Compara; debe ser el nombre completo
class ListarEstBusqueda(ListView):
    template_name='persona/estBusqueda.html'
    context_object_name='estudiantes'
    model=Estudiante

    def get_queryset(self):
        nombre=self.request.GET.get('nombre','')
        #print('Nombre: ', nombre)
        listResultados=Estudiante.objects.filter(primernombre=nombre)
        return listResultados

#Listar estudiantes por habilidades
class ListarEstHabilidad(ListView):
    template_name='persona/estHabilidad.html'
    model=Estudiante
    context_object_name='habilidades'


    def get_queryset(self):
        #estudiante=Estudiante.objects.get(id=2) #Del num Estudiante
        nombre=self.request.GET.get('nombre','')
        #estudiante=Estudiante.objects.get(primernombre=nombre)
        listResultados=Estudiante.objects.filter(primernombre=nombre)
        #print('Nombre: ', nombre)
        print(listResultados)

        #return estudiante.habilidad.all()
        return listResultados

#1 De uno en uno
class EstDetailView(DetailView):
    model=Estudiante
    template_name='persona/detailEst.html'
    
    def get_context_data(self, **kwargs):
       
        context=super(EstDetailView, self).get_context_data(**kwargs)
        context['titulo']='Estudiante'
        return context

#Lista para Muchos
class ListEstFacuView4(ListView):
    model=Facultad
    context_object_name='listaFacultades'
    template_name='persona/intentFAC4.html'

#2 Muchos
class EstDetailViewAll(TemplateView):
    model=Estudiante
    template_name='persona/detailEstAll.html'
    
    def get_context_data(self, **kwargs):
       
        context=super(EstDetailViewAll, self).get_context_data(**kwargs)
        context['titulo']='Información de Estudiantes'
        context['base']=Estudiante.objects.all()
        return context




#Crear
class SuccessView(TemplateView):
    template_name='persona/success.html'

class EstudianteCreateView(CreateView):
    model=Estudiante
    template_name='persona/crearEst.html'
    #fields=('__all__')
    fields=['primernombre','apellido','tipo','facultad','carta','habilidad' ]
    success_url=reverse_lazy('success')

    def form_valid(self, form):
        #hacer validaciones, crear parametros(sin pasar por el html)
        #limpiador de string, etc
        estudiante=form.save()
        estudiante.nombreCompleto=estudiante.primernombre+' '+estudiante.apellido
        estudiante.save()
        return super(EstudianteCreateView, self).form_valid(form)

#Lista para Delete
class ListEstFacuView3(ListView):
    model=Facultad
    context_object_name='listaFacultades'
    template_name='persona/intentFAC3.html'

#Delete
class EstudianteDeleteView(DeleteView):
    model=Estudiante
    template_name='persona/delete.html'
    success_url=reverse_lazy('success')

#Lista para Update
class ListEstFacuView(ListView):
    model=Facultad
    context_object_name='listaFacultades'
    template_name='persona/intentFAC2.html'

#Update
class EstudianteUpdateView(UpdateView):
    model=Estudiante
    template_name='persona/crearEst.html'
    #fields=('__all__')
    fields=['primernombre','apellido','tipo','facultad','carta','habilidad' ]
    success_url=reverse_lazy('success')
    #modf='Estudiante modificado.....'
    #success_url=reverse_lazy('success',kwargs={"modf":modf})

    def form_valid(self, form):
        #hacer validaciones, crear parametros(sin pasar por el html)
        #limpiador de string, etc
        estudiante=form.save()
        estudiante.nombreCompleto=estudiante.primernombre+' '+estudiante.apellido
        estudiante.save()
        return super(EstudianteUpdateView, self).form_valid(form)


#https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-editing/













