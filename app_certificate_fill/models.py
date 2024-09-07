from django.db import models


class Livro(models.Model):
    id_livro = models.AutoField(primary_key=True)
    autor = models.TextField(max_length=255)
    titulo = models.TextField(max_length=255)
    ano = models.IntegerField()
