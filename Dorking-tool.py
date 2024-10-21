import requests
from bs4 import BeautifulSoup
import random
import time
import argparse
import sys
from colorama import Fore, Style, init

#Carga
def mostrar_cargando():
    loading_text = "Cargando urls"
    for i in range(5):
        sys.stdout.write(f"\r{loading_text}{'.' * i}")
        sys.stdout.flush()  # Asegura que el texto se muestre sin esperar el salto de línea
        time.sleep(0.5)
    sys.stdout.write("\r")  # Regresa al inicio de la línea para limpiar el texto al final


# Inicializa colorama
init(autoreset=True)

# Lista de User-Agents
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15',
    # Agrega más User-Agents aquí
]

# Mapeo de motores de búsqueda
search_engines = {
    'Google': 'https://www.google.com/search?q={query}',
    'DuckDuckGo': 'https://duckduckgo.com/?q={query}',
    'Bing': 'https://www.bing.com/search?q={query}',
    #'Yahoo': 'https://search.yahoo.com/search?p={query}',
    'Yandex': 'https://yandex.com/search/?text={query}',
    'Startpage': 'https://www.startpage.com/do/search?query={query}',
}

def search_dorks(query, search_engine, limit=10):
    headers = {
        'User-Agent': random.choice(user_agents)
    }
    
    url = search_engines.get(search_engine)
    links = []
    page_limit = (limit + 9) // 10

    for page in range(page_limit):
        start = page * 10
        paginated_url = url.format(query=query) + f"&start={start}"

        try:
            response = requests.get(paginated_url, headers=headers)
            response.raise_for_status()  # Lanza un error si la respuesta es un código de error
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extrae los enlaces de resultados de búsqueda
            current_page_links = []  # Lista para almacenar los enlaces de la página actual

            # Extrae los enlaces de resultados de búsqueda
            if search_engine == 'Google':
                for item in soup.find_all('h3'):
                    link = item.find_parent('a')['href']
                    current_page_links.append(link)
            elif search_engine == 'DuckDuckGo':
                for item in soup.find_all('a', class_='result__url'):
                    current_page_links.append(link)
            elif search_engine == 'Bing':
                for item in soup.find_all('h2'):
                    link = item.find_parent('a')['href']
                    current_page_links.append(link)
            # elif search_engine == 'Yahoo':
            #     for item in soup.find_all('h3'):
            #         link = item.find_parent('a')['href']
            #         current_page_links.append(link)
            elif search_engine == 'Yandex':
                for item in soup.find_all('a', class_='link'):
                    current_page_links.append(link)
            elif search_engine == 'Startpage':
                for item in soup.find_all('a', class_='result__url'):
                    current_page_links.append(link)

            # Imprime el total de enlaces extraídos de la página actual
            print(f"Total de enlaces extraídos de la página {page + 1}: {len(current_page_links)}")

            links.extend(current_page_links)  # Agrega los enlaces de la página actual a la lista total
            if len(links) == 0:
                break
            if len(links) >= limit:
                break
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f'Error: {e}')
            return []
        
    return links[:limit]

def main():
    parser = argparse.ArgumentParser(description='Herramienta avanzada de Dorking para realizar búsquedas web usando diversos motores de búsqueda.', 
                                     epilog='Usa esta herramienta de manera responsable. El dorking puede ser malinterpretado por algunas plataformas, y ' + Fore.RED + 'BLOQUEAR TU IP',
    formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-q', '--query_file', help='Archivo que contiene las consultas de búsqueda (dorks)', metavar='query_file')
    parser.add_argument('-d', '--dork', help='Uso de un solo dork', metavar='dork')
    parser.add_argument('-e', '--engine', choices=list(search_engines.keys()), default='Google',
                        help='Motor de búsqueda a utilizar (predeterminado: Google)', metavar='engine')
    parser.add_argument('-l', '--limit', type=int, default=10, 
                    help='Número máximo de resultados por búsqueda (predeterminado: 10)', metavar='limite')
    parser.add_argument('-o', '--output', help='Archivo de output de la consulta.', metavar='output FILE')
    parser.add_argument('-p', '--proxy', help='On process' )
    #parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Muestra este mensaje de ayuda.')


    

    args = parser.parse_args()

    # Mostrar la ayuda si no se proporciona ni archivo de dorks ni dork único
    if not args.query_file and not args.dork:
        parser.print_help()
        sys.exit(1)

    # Abrir el archivo de salida si se especifica
    output_file = open(args.output, 'w') if args.output else None

    if args.dork:
        dorks = [args.dork]
    elif args.query_file:
        try:
            with open(args.query_file, 'r') as file:
                dorks = file.readlines()
        except FileNotFoundError:
            print(Fore.RED + f"Error: El archivo '{args.query_file}' no se encontró.")
            return       

    for dork in dorks:
        dork = dork.strip()  # Elimina espacios en blanco y saltos de línea
        print(Fore.CYAN + Style.BRIGHT + f"\nBuscando: {dork} en {Fore.CYAN + args.engine}")
        result_links = search_dorks(dork, args.engine, args.limit)

        if result_links:
            print(Fore.GREEN + f"\nResultados encontrados: {len(result_links)}")
            # Aplicar límite antes de imprimir o guardar
            limited_links = result_links[:args.limit]
            unique_links = set(limited_links)
            print(Fore.CYAN + f"Mostrando hasta {len(limited_links)} enlaces:\n")
            mostrar_cargando()
            for link in unique_links:
                print(Fore.WHITE + link)
                time.sleep(random.uniform(1, 3))  # Espera aleatoria entre 1 y 3 segundos
            if output_file:
                for link in limited_links:
                    output_file.write(f"{link}\n")
        else:
            print(Fore.RED + "No se encontraron resultados. Estas usando el dork correcto?")

    # Cerrar el archivo de salida si fue abierto
    if output_file:
        output_file.close()
    print(Style.RESET_ALL + '\nProceso completado.')





if __name__ == "__main__":
    main()

