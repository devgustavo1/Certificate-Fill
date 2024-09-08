from django.shortcuts import render
from .models import Livro
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LivroSerializer


def home(request):
    return render(request, 'livros/home.html')

def livros(request):
    if request.method == 'POST':
        # Salvar os dados da tela para o banco de dados
        novo_livro = Livro()
        novo_livro.autor = request.POST.get('autor')
        novo_livro.titulo = request.POST.get('titulo')
        novo_livro.ano = request.POST.get('ano')
        
        if novo_livro.autor and novo_livro.titulo and novo_livro.ano:  # Verificar se os campos não estão vazios
            novo_livro.save()
    
    # Exibir todos os livros já cadastrados
    livros = {
        'livros': Livro.objects.all()
    }
    
    # Retornar os dados para a página de listagem de livros
    return render(request, 'livros/livros.html', livros)

@api_view(['GET'])
def livros_api(request):
    livros = Livro.objects.all()
    serializer = LivroSerializer(livros, many=True)
    return Response(serializer.data)