from django.urls import path
from home import views


urlpatterns = [
    path('', views.index, name='index'),
    path('hola/', views.hola, name='hola'),
    path('template/', views.template, name=''),
    path('template/<str:nombre>', views.template_nombre),
    path('prueba-template/', views.prueba_template, name='mi_template'),
    path('nacimiento/<int:edad>', views.calcular_nacimiento),
    path('fecha/', views.fecha, name='fecha'),
    path('ver-familiar/', views.ver_familiar, name='ver_personas'),
    path('nuevo-familiar/<str:nombre>/<str:apellido>/', views.nuevo_familiar),
]

    