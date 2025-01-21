Web Scraper de Notícias de Tecnologia

Um scraper simples desenvolvido em Python para coletar as últimas notícias de tecnologia do site [TechCrunch](https://techcrunch.com/). O projeto exibe as notícias no terminal em formato de tabela interativa e as salva em um arquivo JSON para referência futura.

📋 Funcionalidades

- Acessa automaticamente o site TechCrunch.
- Extrai os títulos e links das 10 notícias mais recentes.
- Exibe os resultados em uma tabela colorida no terminal usando a biblioteca `rich`.
- Salva as notícias extraídas em um arquivo JSON.

🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal para o desenvolvimento.
- **Requests**: Para realizar requisições HTTP ao site.
- **BeautifulSoup**: Para fazer o scraping e análise do HTML.
- **Rich**: Para melhorar a exibição no terminal com tabelas e cores.
- **JSON**: Para salvar os dados em um arquivo.

🚀 Como Executar o Projeto

Pré-requisitos

- **Python 3.7+** instalado no computador.
- Instalar as bibliotecas necessárias:
  ```bash
  pip install requests beautifulsoup4 rich
