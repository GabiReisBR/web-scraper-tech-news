import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
import json

# URL do site de notícias de tecnologia
URL = "https://techcrunch.com/"

# Função para salvar as notícias em um arquivo JSON
def save_to_json(news_list, filename="news.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(news_list, file, ensure_ascii=False, indent=4)
    print(f"As notícias foram salvas no arquivo: {filename}")

# Função principal do scraper
def scrape_tech_news():
    console = Console()

    try:
        # Fazendo a requisição HTTP
        response = requests.get(URL)
        response.raise_for_status()

        # Parse do conteúdo HTML com BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Selecionando os títulos das notícias
        headlines = soup.find_all('h3', class_='loop-card__title')

        if not headlines:
            console.print("[bold red]Nenhuma notícia encontrada. Verifique o seletor.[/bold red]")
        else:
            # Criando uma tabela para exibir os dados
            table = Table(title="Últimas Notícias em Tecnologia", show_lines=True)

            # Adicionando colunas
            table.add_column("No.", style="bold cyan", justify="center")
            table.add_column("Título", style="bold yellow")
            table.add_column("Link", style="bold green")

            # Lista para salvar as notícias
            news_list = []

            # Adicionando linhas com as notícias
            for i, headline in enumerate(headlines[:10], start=1):
                title = headline.text.strip()
                link = headline.a['href']
                table.add_row(str(i), title, link)

                # Adicionando os dados à lista
                news_list.append({"no": i, "title": title, "link": link})

            # Exibindo a tabela
            console.print(table)

            # Salvando em JSON
            save_to_json(news_list)

    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Erro ao acessar o site: {e}[/bold red]")

# Executar o scraper
if __name__ == "__main__":
    scrape_tech_news()
