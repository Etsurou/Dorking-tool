# Dorking-tool

Una herramienta avanzada de dorking para realizar búsquedas web utilizando diversos motores de búsqueda. Este proyecto está diseñado para facilitar la búsqueda de información específica en la web, utilizando dorks que permiten filtrar resultados de manera eficiente.

## Tabla de Contenidos

- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)
- [Opciones de Comando](#opciones-de-comando)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Características

- Realiza búsquedas en múltiples motores de búsqueda como Google, DuckDuckGo, Bing, Yandex y Startpage.
- Extrae enlaces de resultados de búsqueda y los guarda en un archivo de salida.
- Permite el uso de proxies para búsquedas anónimas.
- Muestra resultados de manera organizada y fácil de leer.

## Instalación

1. Asegúrate de tener Python 3 instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
2. Clona este repositorio:

   ```bash
   git clone https://github.com/Etsurou/Dorking-tool.git
Navega a la carpeta del proyecto:

bash
Copiar código
cd Dorking-tool
Instala las dependencias necesarias

pip install -r requirements.txt

Uso
Puedes utilizar la herramienta a través de la línea de comandos. Aquí hay un ejemplo de cómo ejecutarla:

python dorking_tool.py -d "tu_dork_aqui" -e Google -l 10 -o resultados.txt
Ejemplo de uso:
python dorking_tool.py -q dorks.txt -e DuckDuckGo -l 20 -o resultados.txt
Opciones de Comando
-q, --query_file: Archivo que contiene las consultas de búsqueda (dorks).
-d, --dork: Uso de un solo dork.
-e, --engine: Motor de búsqueda a utilizar (predeterminado: Google).
-l, --limit: Número máximo de resultados por búsqueda (predeterminado: 10).
-o, --output: Archivo de salida para guardar los resultados.
-p, --proxy: Uso de un proxy para búsquedas anónimas.
Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar esta herramienta, siéntete libre de hacer un fork del repositorio y enviar un pull request.

Licencia
Este proyecto está licenciado bajo la MIT License.

¡Usa esta herramienta de manera responsable! El dorking puede ser malinterpretado por algunas plataformas.
