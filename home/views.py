from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render
import random

from home.models import Familiar

def hola(request):
                
    return HttpResponse('<h1>Hola</h1>')

def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f'La fecha actual es {fecha_y_hora}')

def calcular_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu fecha de nacimiento aproximada para tus {edad} años sería: {fecha}')

def template(request):
    cargar_archivo = open(r'C:\Users\manue\Downloads\entregaCoder\entregaCoder\templates\mi_template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

def template_nombre(request, nombre):
    template = loader.get_template('home/template_nombre.html')
    template_renderizado = template.render({'persona': nombre})
    return HttpResponse(template_renderizado)

def prueba_template(request):
    
    mi_contexto = {
        'rango' : list(range(1,11)),
        'valor_aleatorio' : random.randrange(1,11)
        }
    template = loader.get_template('home/prueba_template.html')
    template_renderizado = template.render(mi_contexto)
    return HttpResponse(template_renderizado)

def nuevo_familiar(request, nombre, apellido):
    
    familiar = Familiar(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_de_creacion=datetime.now())
    familiar.save()
    
    # template = loader.get_template('home/nuevo_familiar.html')
    # template_renderizado = template.render({'familiar': familiar})
    # return HttpResponse(template_renderizado)

    return render(request, 'home/nuevo_familiar.html', {'familiar': familiar})

def ver_familiar(request):
    
    familiares = Familiar.objects.all()
    
    # template = loader.get_template('ver_familiar.html')
    # template_renderizado = template.render({'familiares': familiares})
    # return HttpResponse(template_renderizado)
    
    return render(request, 'home/ver_familiar.html', {'familiares': familiares})

def index(request):
    
    return render(request, 'home/index.html')