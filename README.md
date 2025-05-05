# WebScrapingTeste

#Scraper de Produto 

#Índice

* [Sobre o Projeto](#sobre-o-projeto)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Instalação](#instalação)
* [Como Usar](#como-usar)
* [Formato da Saída](#formato-da-saída)
* [Licença](#licença)


#Sobre o Projeto

Este projeto foi desenvolvido para o desafio técnico da **Infosimples**, com o objetivo de extrair dados estruturados de uma página HTML de produto.

O scraper coleta as seguintes informações:

* Título do produto
* Marca
* Categorias
* Descrição
* Variações (SKUs) com preços e disponibilidade
* Propriedades do produto
* Avaliações dos clientes
* Nota média
* URL da página

O script utiliza a biblioteca `BeautifulSoup` para parseamento do HTML e `requests` para acesso ao conteúdo.

---

# Tecnologias Utilizadas

* [Python 3.x](https://www.python.org/)
* [requests](https://docs.python-requests.org/)
* [BeautifulSoup (bs4)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [json](https://docs.python.org/3/library/json.html)

---

#⚙️ Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/scraper-infosimples.git
   cd scraper-infosimples
   ```

2. Crie um ambiente virtual (opcional):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install requests beautifulsoup4
   ```

---

#Como Usar

1. Execute o script principal:

   ```bash
   python scraper.py
   ```

2. Um arquivo chamado `produto.json` será gerado com os dados extraídos.

---

#Formato da Saída

O arquivo `produto.json` segue este modelo:

```json
{
  "title": "Nome do Produto",
  "brand": "Marca",
  "categories": ["Categoria 1", "Categoria 2"],
  "description": "Descrição do produto...",
  "skus": [
    {
      "name": "Variante 1",
      "current_price": 149.9,
      "old_price": 199.9,
      "available": true
    }
  ],
  "properties": [
    {"label": "Cor", "value": "Preto"},
    {"label": "Material", "value": "Algodão"}
  ],
  "reviews": [
    {
      "name": "Usuário",
      "date": "10/04/2024",
      "score": 5,
      "text": "Excelente produto!"
    }
  ],
  "reviews_average_score": 4.6,
  "url": "https://infosimples.com/vagas/desafio/commercia/product.html"
}
```

---

#Licença

Este projeto está sob a licença MIT. 
