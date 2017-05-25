from django.db import models
from django.utils import timezone


class Post(models.Model):
    autor = models.ForeignKey('Autor')
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publicado_data = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.nome
