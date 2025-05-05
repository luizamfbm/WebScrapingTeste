import requests
from bs4 import BeautifulSoup
import json

#Pegando a página do produto
link = 'https://infosimples.com/vagas/desafio/commercia/product.html'
resposta = requests.get(link)
html = resposta.content
soup = BeautifulSoup(html, 'html.parser')

#Tentando extrair o título da aba do navegador
titulo_bruto = soup.find('title')
if titulo_bruto:
    titulo_texto = titulo_bruto.get_text().strip()
    titulo = titulo_texto.split('|')[0].strip()
else:
    titulo = None

#Pegando a marca
marca_div = soup.find('div', class_='brand')
marca = marca_div.text.strip() if marca_div else None

#Categorias (corrigido para refletir a estrutura real da <nav>)
categorias = []
nav_categoria = soup.find('nav', class_='current-category')
if nav_categoria:
    links_categoria = nav_categoria.find_all('a')
    categorias = [a.get_text(strip=True) for a in links_categoria if a.get_text(strip=True)]

#Descrição geral
meta_descricao = soup.select_one('meta[itemprop=description]')
descricao = meta_descricao['content'].strip() if meta_descricao else None

#Variantes do produto
skus = []
cartoes = soup.select('div.card-container')
for cartao in cartoes:
    nome = cartao.select_one('div.prod-nome')
    preco_atual = cartao.select_one('div.prod-pnow')
    preco_antigo = cartao.select_one('div.prod-pold')

    nome_produto = nome.get_text(strip=True) if nome else None

    if preco_atual and preco_atual.text.strip():
        atual = float(preco_atual.text.replace('R$', '').replace(',', '.').strip())
    else:
        atual = None

    if preco_antigo and preco_antigo.text.strip():
        antigo = float(preco_antigo.text.replace('R$', '').replace(',', '.').strip())
    else:
        antigo = None

    disponivel = atual is not None

    skus.append({
        'name': nome_produto,
        'current_price': atual,
        'old_price': antigo,
        'available': disponivel
    })

#Pegando as propriedades da tabela
propriedades = []
titulo_tabela = soup.find('h4', string=lambda txt: txt and 'Product properties' in txt)
if titulo_tabela:
    tabela = titulo_tabela.find_next('table')
    linhas = tabela.find_all('tr') if tabela else []
    for linha in linhas:
        colunas = linha.find_all('td')
        if len(colunas) == 2:
            chave = colunas[0].text.strip()
            valor = colunas[1].text.strip()
            propriedades.append({'label': chave, 'value': valor})

#Comentários dos clientes
avaliacoes = []
blocos = soup.select('div.analisebox')
for bloco in blocos:
    usuario = bloco.select_one('span.analiseusername')
    data = bloco.select_one('span.analisedate')
    estrelas = bloco.select_one('span.analisestars')
    comentario = bloco.select_one('p')

    nota = estrelas.get_text(strip=True).count('★') if estrelas else 0

    avaliacoes.append({
        'name': usuario.get_text(strip=True) if usuario else None,
        'date': data.get_text(strip=True) if data else None,
        'score': nota,
        'text': comentario.get_text(strip=True) if comentario else None
    })

#Nota média
media = 0.0
titulo_media = soup.find('h4', string=lambda t: t and 'Average score' in t)
if titulo_media:
    try:
        texto = titulo_media.get_text()
        media = float(texto.split(':')[1].split('/')[0].strip())
    except:
        media = 0.0

#Juntando tudo
saida = {
    'title': titulo,
    'brand': marca,
    'categories': categorias,
    'description': descricao,
    'skus': skus,
    'properties': propriedades,
    'reviews': avaliacoes,
    'reviews_average_score': round(media, 2),
    'url': link
}

#Salvando como JSON
with open('produto.json', 'w', encoding='utf-8') as arquivo:
    json.dump(saida, arquivo, indent=2, ensure_ascii=False)

print('JSON salvo com sucesso!')
