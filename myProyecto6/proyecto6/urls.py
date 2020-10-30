from django.contrib import admin
from django.urls import path, include
from .views import index,galeria,servicios,vision,formulario,registroProductos,login,cerrar_sesion,lista_insumos,eliminar,busqueda_mod,modificar


urlpatterns = [
    path('',index,name='IND'),
    path('galeria#galeria/',galeria, name='GALE'),
    path('servicios#producto/',servicios,name='SERV'),
    path('vision#expertos/',vision,name='VIS'),
    path('formulario/',formulario, name='FORM'),
    path('registroProductos/',registroProductos, name='REG'),
    path('login/',login,name='LOG'),
    path('cerrar_sesion/',cerrar_sesion,name='LOGOUT'),
    path('lista_insumos/',lista_insumos,name='LISTAINSUMOS'),
    path('eliminar/<id>/',eliminar,name='ELIMINAR'),
    path('buscar/<id>/',busqueda_mod,name='BUSCAR'),
    path('modificar/',modificar,name='MODIFICAR'),
]