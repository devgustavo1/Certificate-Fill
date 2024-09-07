from django.shortcuts import render
from .models import Livro


def home(request):
    return render(request, 'livros/home.html')


def livros(request):
    # Salvar os dados da tela para o banco de dados
    novo_livro = Livro()
    novo_livro.autor = request.POST.get('autor')
    novo_livro.titulo = request.POST.get('titulo') 
    novo_livro.ano = request.POST.get('ano') 
    novo_livro.save()
    # Exibir todos os livros já cadastrados em uma nova página
    livros = {
        'livros': Livro.objects.all()
    }
    # Retornar os dados para a página de listagem de usuários
    return render(request, 'livros/livros.html', livros)