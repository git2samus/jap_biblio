from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User


class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)

    prestado = models.ForeignKey(User, null=True, blank=True)
    fecha_devolucion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Libro <{} ({})>".format(self.titulo, self.isbn)

    def get_absolute_url(self):
        return reverse('libro', args=(self.id,))
