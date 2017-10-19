from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from web.models import Libro

# Create your views here.
def libro(request, numero_libro):
    #libro = Libro.objects.get(id=numero_libro)
    libro = get_object_or_404(Libro, id=numero_libro)
    #return HttpResponse("{} ({})".format(libro.titulo, libro.isbn))
    return render(request, 'libro.html', context={'libro': libro})
