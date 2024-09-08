from rest_framework import serializers
from .models import Livro

# permite que você serialize (converta) os dados do seu modelo Livro de uma maneira automática.
class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id_livro', 'autor', 'titulo', 'ano']