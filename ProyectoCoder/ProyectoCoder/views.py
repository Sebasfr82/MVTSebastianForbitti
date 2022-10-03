from AppCoder.models import Familiar
from django.template import loader
from django.http import HttpResponse

def registrar (request):
    familiar01=Familiar.objects.create(nombre="Sebastian", Salario="500", fechadeNacimiento="1982-10-11")
    familiar02=Familiar.objects.create(nombre="Luciana", Salario="300", fechadeNacimiento="1986-12-18")
    familiar03=Familiar.objects.create(nombre="Catalina", Salario="100", fechadeNacimiento="2015-03-11")
    familiar04=Familiar.objects.create(nombre="Juan Cruz", Salario="100", fechadeNacimiento="2018-03-10")
    template = loader.get_template("templates01.html")
    diccionario = {
        "nombre01":familiar01.nombre,
        "nombre02":familiar02.nombre, 
        "nombre03":familiar03.nombre, 
        "nombre04":familiar04.nombre,
        "salario01":familiar01.Salario,
        "salario02":familiar02.Salario,
        "salario03":familiar03.Salario,
        "salario04":familiar04.Salario,
        "fechadenacimiento01":familiar01.fechadeNacimiento,
        "fechadenacimiento02":familiar02.fechadeNacimiento,
        "fechadenacimiento03":familiar03.fechadeNacimiento,
        "fechadenacimiento04":familiar04.fechadeNacimiento,

        }
    res = template.render(diccionario)
    return HttpResponse(res)

