from django.urls import path
from home import views


urlpatterns = [
    path('', views.index),
    path('hola/', views.hola),
    path('template/', views.template),
    path('template/<str:nombre>', views.template_nombre),
    path('prueba-template/', views.prueba_template),
    path('nacimiento/<int:edad>', views.calcular_nacimiento),
    path('fecha/', views.fecha),
    path('ver-familiar/', views.ver_familiar),
    path('nuevo-familiar/<str:nombre>/<str:apellido>/', views.nuevo_familiar),
]

    