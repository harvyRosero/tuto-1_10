from datetime import datetime
from pipes import Template
from urllib.request import Request
from django.http import HttpResponse
from django.template import Context, Template
from django.template.loader import get_template
from django.shortcuts import render


class Persona(object):
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request):
    # doc_externo = open("C:/Users/Adriana/Documents/py/django/Proyecto1/Proyecto1/plantillas/mi.html")
    # plt = Template(doc_externo.read()) 
    # doc_externo.close()
    
    ahora = datetime.now()
    temas_curso = ["plantillas", "modelas", "formularios", "vistas", "despliegue"]
    p1 = Persona("Harvy Santiago", "Rosero")
    ctx = Context( {"nombre": p1.nombre, "apellido": p1.apellido, "actual": ahora, } )
    
    # documento = plt.render(ctx)
    
    # doc_externo = get_template("mi.html")
    # documento = doc_externo.render( {"nombre": p1.nombre, "apellido": p1.apellido, "actual": ahora, 
                                            #  "temas": temas_curso } )
    
    return render(request, "mi.html", {"nombre": p1.nombre, "apellido": p1.apellido, "actual": ahora,
                                       "temas": temas_curso })

def cursoC (request):
    fecha = datetime.now()
    return render(request, "curso.html", {"fecha": fecha})

def cursoCSS (request):
    fecha = datetime.now()
    return render(request, "cursocss.html", {"fecha": fecha})

def despedida(request):
    return HttpResponse('Adios mundo')


def fecha(request):
    from datetime import datetime
    ahora = datetime.now()
    
    documento = """
    
    <html>
    <body>
    <h1> fecha y hora actuales %s </h1> 
    </body>
    </html>
    """ % format(ahora)
    
    return HttpResponse(documento)


def calcula_edad(request, edad,  agno):
    # edad_actual = 22
    periodo = agno - 2022
    edad_futura = edad + periodo 
    
    documento = """
    <html>
    <body>
    <h2> En el año %s tendrás %s años </h2> 
    </body>
    </html>
    """ % (agno, edad_futura)
    
    return HttpResponse(documento)