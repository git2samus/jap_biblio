from django.db import models
from django.urls import reverse


class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)

    prestado = models.BooleanField()

    def __str__(self):
        return "Libro <{} ({})>".format(self.titulo, self.isbn)

    def get_absolute_url(self):
        return reverse('libro', args=(self.id,))
