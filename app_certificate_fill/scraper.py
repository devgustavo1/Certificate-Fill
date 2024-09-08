from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://en.wikipedia.org/wiki/List_of_best-selling_books')
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
        print(f"Esse é o livro: {titulo} - {autor} - {ano}")
        livros_raspados.append((titulo, autor, ano))
    else:
        print("Linha com número inesperado de células:", row.text)

time.sleep(3)
try:
    driver.get('http://127.0.0.1:8000/')
except Exception as e:
    print("Problema para acessar URL local:", e)


driver.quit()