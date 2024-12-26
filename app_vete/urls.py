from django.contrib import admin
from django.urls import path

from app_vete import views

urlpatterns = [

    #Mostrar perfil, editar perfil, cambiar contraseña
    path('mostrar-perfil/', views.mostrar_perfil, name = "mostrar-perfil"),
    path('editar-perfil/', views.editar_perfil, name = "editar-perfil"),
    path('cambiar-contraseña/', views.cambiar_contraseña, name = "cambiar-contraseña"),
    

    #Inicio de sesion, registro, cerrar sesion
    path('inicio-sesion/', views.inicio_sesion, name = "inicio-sesion"),
    path('cerrar-sesion/', views.cerrar_sesion, name = "cerrar-sesion"),
    path('registro-usuario/', views.registro_usuario, name = "registro-usuario"),
    path('registro-exitoso-usuario/', views.registro_exitoso_usuario, name = "registro-exitoso-usuario" ),

    #Vistas Inicio
    path('', views.inicio, name = "inicio"),
    path('sucursal/', views.sucursal, name = "sucursal"),
    path('producto/', views.producto, name = "producto"),
    path('cliente/', views.cliente, name = "cliente"),
    path('mascota/', views.mascota, name = "mascota"),
    path('acerca/', views.acerca, name = "acerca"),


    #Formularios
    path('mascota-form/', views.formulario_mascota, name = "mascota-form" ),
    path('cliente-form/', views.formulario_cliente, name = "cliente-form" ),
    path('producto-form/', views.formulario_producto, name = "producto-form" ),
    path('sucursal-form/', views.formulario_sucursal, name = "sucursal-form" ),
    path('registro-exitoso/', views.registro_exitoso, name = "registro-exitoso" ),
    
    #Delete
    path('eliminar-producto/<int:id>', views.eliminar_producto, name = "delete-producto"),
    path('eliminar-mascota/<int:id>', views.eliminar_mascota, name = "delete-mascota"),
    path('eliminar-cliente/<int:id>', views.eliminar_cliente, name = "delete-cliente"),
    path('eliminar-sucursal/<int:id>', views.eliminar_sucursal, name = "delete-sucursal"),

    #Editar
    path('editar-sucursal/<int:id>', views.editar_sucursal, name = "editar-sucursal"),
    path('editar-mascota/<int:id>', views.editar_mascota, name = "editar-mascota"),
    path('editar-cliente/<int:id>', views.editar_cliente, name = "editar-cliente"),
    path('editar-producto/<int:id>', views.editar_producto, name = "editar-producto"),

    #Descripcion
    path('descripcion-producto/<int:id>', views.descripcion_producto, name = "descripcion-producto"),
]