from django.urls import path
from . import views

urlpatterns = [
    path('facultad', views.facultad, name='facultad'),
    path('listaFacultades', views.ListarFacultades.as_view(), name='listaFacultades'),

    path('listFacuBusqueda', views.ListarFacuBusqueda.as_view(), name='listFacuBusqueda'),
    path('listFacuActiva', views.ListarFacuActiva.as_view(), name='listFacuActiva'),
    #Detalle de Facultad
    path('EstFacu4List', views.EstFacuView4List.as_view(), name='EstFacu4List'),
    path('detailFacu/<pk>', views.FacuDetailView.as_view(), name='detailFacu'),

    #Crear
    path('crearFacu', views.FacultadCreateView.as_view(), name='crearFacu'),
    path('successFacu', views.SuccessView.as_view(), name='successFacu'),
    #Delete
    path('EstFacu3List', views.EstFacuView3List.as_view(), name='EstFacu3List'),
    path('deleteFacu/<pk>', views.FacultadDeleteView.as_view(), name='deleteFacu'),
    #Update
    path('EstFacu2List', views.EstFacuView2List.as_view(), name='EstFacu2List'),
    path('updateFacu/<pk>', views.FacultadUpdateView.as_view(), name='updateFacu'),

    path('idFacu', views.idFacultad, name='idFacu'),

    path('detailFacuAll', views.FacuDetailViewAll.as_view(), name='detailFacuAll'),

]
