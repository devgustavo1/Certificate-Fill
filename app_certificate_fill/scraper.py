from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import requests

driver = webdriver.Chrome()

def rpa_visual(livros_raspados):
    print("Começando automação visual.")
    for livro in livros_raspados:
        driver.get('http://127.0.0.1:8000/')
        time.sleep(2)
        add_autor = livro[1]
        add_titulo = livro[0]
        add_ano = livro[2]
        time.sleep(1)
        pyautogui.click(x=646,y=292)
        pyautogui.write(add_autor)

        time.sleep(0.5)
        pyautogui.click(x=869,y=290)
        pyautogui.write(add_titulo)

        time.sleep(0.5)
        pyautogui.click(x=1082,y=291)
        pyautogui.write(add_ano)

        time.sleep(1)
        pyautogui.click(x=1285,y=288,button='left')

    print(f"Encerrando automação via RPA (visual).")
    driver.quit()

def rpa_headless(livros_raspados):
    options = Options()
    options.add_argument('--headless')  # Ativa o modo headless
    options.add_argument('--disable-gpu')  # Desativa a GPU (recomendado para headless)
    options.add_argument('--no-sandbox')  # Desativa o sandbox (necessário em alguns ambientes)

    driver = webdriver.Chrome(options=options)
    print("Começando automação headless.")
    try:
        for livro in livros_raspados[5:]:  # Começando do 6º livro em diante
            # Acessar a página de formulário
            driver.get('http://127.0.0.1:8000/')
            
            # Aguardar que os campos do formulário estejam visíveis
            input_titulo = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/form/div/input[1]'))
            )
            input_autor = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/form/div/input[2]'))
            )
            input_ano = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/form/div/input[3]'))
            )
            
            # Preencher os campos com os dados raspados
            input_titulo.clear()
            input_titulo.send_keys(livro[0])

            input_autor.clear()
            input_autor.send_keys(livro[1])

            input_ano.clear()
            input_ano.send_keys(livro[2])

            # Encontrar e clicar no botão de submissão
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/form/div/button'))
            )
            submit_button.click()
            print(f"Livro {livro[0]} adicionado no modo HEADLESS.")
            # Aguardar um pouco para garantir que a ação foi concluída
            time.sleep(2)

        print("Automação headless concluída.")
    except Exception as e:
        print(f"Problema para acessar URL local: {e}")
    finally:
        driver.quit()

driver.get('https://en.wikipedia.org/wiki/List_of_best-selling_books')
driver.maximize_window()
time.sleep(3)

# Encontrar elementos na página
table = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[4]')
header_rows = table.find_elements(By.XPATH, './/thead/tr')
header_columns = header_rows[0].find_elements(By.TAG_NAME, 'th') #cabeçalho
# Iterar pelas linhas da tabela e imprimir os dados
rows = table.find_elements(By.XPATH, './/tbody/tr')
livros_raspados = []

for row in rows: 
    cells = row.find_elements(By.TAG_NAME, 'td')
    if len(cells) >= 3: 
        titulo = cells[0].text 
        autor = cells[1].text
        ano = cells[3].text
        print(f"Obtido: {titulo} - {autor} - {ano}")
        livros_raspados.append((titulo, autor, ano))
    else:
        print("Linha com número inesperado de células:", row.text)
print("Raspagem concluída.")
print()
time.sleep(1)

try:
    rpa_visual(livros_raspados[:5])
    time.sleep(1)
except Exception as e:
    print("Problema para capturar no modo visual:", e)

try:
    rpa_headless(livros_raspados[5:25])
except Exception as e:
    print("Problema para capturar no modo headless:", e)
