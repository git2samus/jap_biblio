from datetime import datetime, timedelta
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from web.models import Libro

def listado(request):
    query = Libro.objects.all()
    return render(request, 'listado.html', context={'listado': query})


def libro(request, numero_libro):
    libro = get_object_or_404(Libro, id=numero_libro)

    mensaje = ""
    if request.method == 'POST':
        if request.POST['accion'] == 'prestar':
            if request.user.is_authenticated:
                libro.prestado = request.user
                libro.fecha_devolucion = datetime.utcnow() + timedelta(days=15)
            else:
                mensaje = "Quien te conoce papá? Anda a loguearte ñeri"
        else:
            libro.prestado = None
            libro.fecha_devolucion = None
        libro.save()

    return render(request, 'libro.html', context={'libro': libro, 'msg': mensaje})
