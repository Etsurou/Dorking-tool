# Dorking Tool

## Descripción
Esta herramienta de dorking permite realizar búsquedas avanzadas en varios motores de búsqueda utilizando dorks específicos. Es útil para encontrar información expuesta públicamente en la web.

## Características

- **Múltiples Motores de Búsqueda**: Soporte para Google, DuckDuckGo, Bing, Yandex y Startpage.
- **Interfaz de Línea de Comandos**: Fácil de usar con argumentos para personalizar las búsquedas.
- **Extracción de Enlaces**: Recopila enlaces relevantes según las consultas proporcionadas.
- **Soporte para Proxies**: Opción para realizar búsquedas de manera anónima.
- **Manejo de Errores**: Notificaciones claras sobre problemas de conexión o respuestas vacías.

## Requisitos

- Python 3.6 o superior
- Paquetes de Python:
  - `requests`
  - `beautifulsoup4`
  - `colorama`
  
Puedes instalar los paquetes requeridos con:

```bash
pip install requests beautifulsoup4 colorama
```
o ejecutando el requirement.txt

```bash
pip install -r requirement.txt
```

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/Etsurou/Dorking-tool.git
   ```

2. Navega a la carpeta del proyecto:

   ```bash
   cd Dorking-tool
   ```

3. Instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

Puedes utilizar la herramienta a través de la línea de comandos. Aquí hay un ejemplo de cómo ejecutarla:

```bash
python Dorking_tool.py -d "tu_dork_aqui" -e Google -l 10 -o resultados.txt
```

### Ejemplo de uso:

```bash
python Dorking_tool.py -q dorks.txt -e DuckDuckGo -l 20 -o resultados.txt
```

## Opciones de Comando

- `-q, --query_file`: Archivo que contiene las consultas de búsqueda (dorks).
- `-d, --dork`: Uso de un solo dork.
- `-e, --engine`: Motor de búsqueda a utilizar (predeterminado: Google).
- `-l, --limit`: Número máximo de resultados por búsqueda (predeterminado: 10).
- `-o, --output`: Archivo de salida para guardar los resultados.
- `-p, --proxy`: Uso de un proxy para búsquedas anónimas.

## Licencia

Este proyecto está licenciado bajo la MIT License.

¡Usa esta herramienta de manera responsable! El dorking puede ser malinterpretado por algunas plataformas, y tu ip puede ser baneada.
