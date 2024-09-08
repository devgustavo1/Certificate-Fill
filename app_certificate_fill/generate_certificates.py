import requests
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

print("Começando script. ")

def fetch_books():
    url = 'http://127.0.0.1:8000/api/livros/'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch books: {response.status_code}")

def generate_certificates(lista_livros_api):
    if not lista_livros_api:
        print("Nenhum livro recebido.")
        return

    caminho_fonte = r"C:\windows\fonts\ARIALN.TTF"
    try:
        font = ImageFont.truetype(caminho_fonte, 24)
    except IOError:
        print("Fonte não encontrada. Usando fonte padrão.")
        font = ImageFont.load_default()

    # Diretório para salvar os certificados
    cert_dir = Path("generated_certificates")
    cert_dir.mkdir(parents=True, exist_ok=True)

    lista_livros = lista_livros_api
    for livro in lista_livros:
        ano = livro.get("ano", "Desconhecido")
        titulo = livro.get("titulo", "Sem Título")
        autor = livro.get("autor", "Desconhecido")
        id_livro = livro.get("id_livro", "sem_id")

        width, height = 800, 600
        background_color = (255, 255, 255)  # Branco
        rgb_preto = (0, 0, 0)
        image = Image.new('RGB', (width, height), background_color)
        draw = ImageDraw.Draw(image)
        text = f"Autor: {autor}\nTítulo: {titulo}\nAno: {ano}"
        text_position = (50, 50)  # Posição (x, y) do texto

        draw.text(text_position, text, fill=rgb_preto, font=font)
        nome_livro = f"{id_livro}-{titulo}-{autor}".replace('/', '_').replace('\\', '_') # evitando caracteres problematicos para salvar
        caminho_arquivo = cert_dir / f"{nome_livro}.png"

        if caminho_arquivo.is_file():
            print(f"{nome_livro} já existe.")
        else:
            print(f"Salvando '{nome_livro}' na pasta.")
            image.save(caminho_arquivo)

    print("Encerrando a geração.")
  

lista_livros_api = fetch_books()
generate_certificates(lista_livros_api)




