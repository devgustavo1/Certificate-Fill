# Projeto de Automação de Livros

Este projeto automatiza o processo de inserção de dados de livros em uma aplicação web e a geração de certificados usando Python e ferramentas de automação RPA. O fluxo do projeto é descrito abaixo:

## Fluxo do Projeto

### **Início**

O processo começa com o arquivo `scraper.py`.

### **Raspagem de Dados (Wikipedia)**

- **Descrição**: A função `scraper.py` utiliza Selenium para raspar dados da página da Wikipedia.
- **Dados Coletados**: Título, autor e ano dos livros.

### **Processamento dos Dados Raspados**

- **Armazenamento**: Os dados raspados são armazenados na lista `livros_raspados`.

### **Automação Visual (RPA Visual)**

- **Descrição**: Função utilizada somente para os 5 primeiros livros na lista (afim de demonstrar diferentes métodos):
  - **Função**: `rpa_visual()`
  - **Ferramenta**: PyAutoGUI
  - **Ação**: Insere os dados visivelmente no formulário de uma página web local.
  - **Redirecionamento**: Após a inserção de cada livro, o navegador é redirecionado para a página inicial.
  - **Conclusão**: Finaliza após todos os livros selecionados serem inseridos.

### **Automação Headless (RPA Headless)**

- **Descrição**: Função utilizada para inserir do quinto livro em diante:
  - **Função**: `rpa_headless()`
  - **Ferramenta**: Selenium no modo headless
  - **Ação**: Preenche e submete os dados diretamente no formulário, sem exibição visual.
  - **Redirecionamento**: Após a inserção de cada livro, o navegador retorna à página de adição.

### **Conclusão da Automação**

- **Descrição**: Após todos os livros serem inseridos na aplicação local, o processo continua para a geração de certificados, que tem o módulo executado pela biblioteca subprocess.

### **Geração de Certificados**

- **Script**: `generate_certificates.py`
- **Descrição**:
  - Consulta a API da aplicação local para obter os dados dos livros cadastrados.
  - Gera um certificado de imagem para cada livro.
  - Salva os certificados localmente.

### **Fim**

O processo se encerra após a criação e armazenamento dos certificados.

---

## **Como Executar**

1. **Instalação das Dependências**: Instale as bibliotecas necessárias listadas no `requirements.txt`.
2. **Executando o Django**: Execute `python .\manage.py runserver` para rodar.
2. **Raspagem de Dados**: Execute `scraper.py` para coletar dados da Wikipedia.
3. **Automação**: Utilize `rpa_visual()` para os primeiros 5 livros e `rpa_headless()` para os demais.
4. **Geração de Certificados**: Execute `generate_certificates.py` para gerar e salvar os certificados.

---


