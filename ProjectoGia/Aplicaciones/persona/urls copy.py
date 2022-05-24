from django.urls import path
from . import views



urlpatterns = [
    path('estudiantes', views.estudiantes, name='estudiantes'),
    path('listaEstudiantes', views.ListarEstudiantes.as_view(), name='listaEstudiantes'),

    path('listEstFacu/<facultad>', views.ListarEstFacu.as_view(), name='listEstFacu'),



    #Opcion1 FacuEst
    path('facuEstudents', views.facuEstudiantes, name='facuEstudiantes'),

    path('listEstBusqueda', views.ListarEstBusqueda.as_view(), name='listEstBusqueda'),
    path('listEstHabilidad', views.ListarEstHabilidad.as_view(), name='listEstHabilidad'),
    #Detalle por estudiante
    path('detailEst/<pk>', views.EstDetailView.as_view(), name='detailEst'),
    path('listFaculEst4', views.ListEstFacuView.as_view(), name='listFaculEst4'),
    path('listEstFacu4/<facultad>', views.ListarEstFacu2.as_view(), name='listEstFacu4'),

    path('detailEstAll', views.EstDetailViewAll.as_view(), name='detailEstAll'),
    #Crear
    path('crearEst', views.EstudianteCreateView.as_view(), name='crearEst'),
    path('success', views.SuccessView.as_view(), name='success'),
    #Update
    path('listFaculEst2', views.ListEstFacuView.as_view(), name='listFaculEst2'),
    path('listEstFacu2/<facultad>', views.ListarEstFacu2.as_view(), name='listEstFacu2'),
    path('updateEst/<pk>', views.EstudianteUpdateView.as_view(), name='updateEst'),
    #Delete
    path('listFaculEst3', views.ListEstFacuView3.as_view(), name='listFaculEst3'),
    path('listEstFacu3/<facultad>', views.ListarEstFacu3.as_view(), name='listEstFacu3'),
    path('deleteEst/<pk>', views.EstudianteDeleteView.as_view(), name='deleteEst'),

    path('idEst', views.intento1, name='idEst'),
    path('listFaculEst', views.ListarFacultades.as_view(), name='listFaculEst'),
    path('idEst2', views.intento2.as_view(), name='idEst2'),
    



]
