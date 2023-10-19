import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


pagina = requests.get('https://www.maze.com.br/categoria/sale/tenis', headers=headers)

conteudo = pagina.content

site = BeautifulSoup(conteudo, 'html.parser')

body = site.find("body")

grid = body.find("div", class_="type-grid")

product_container = grid.find_all("div", class_="content")

produtos = []

for produto in product_container:
  title = produto.find_all('span')[0].text

  old_price = produto.find('span', class_="precoBase").text

  price = produto.find_all('span')[3].text

  link = produto.find('a')['href'].strip()

  print('Produto: ', title.strip())
  print('Preço antigo: ', old_price)
  print('Preço Atual R$: ', price)
  print(f'Link: maze.com.br{link}')
  print( )
