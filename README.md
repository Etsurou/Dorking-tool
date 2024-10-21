# Dorking Tool

## Descripción
Esta herramienta de dorking permite realizar búsquedas avanzadas en varios motores de búsqueda utilizando dorks específicos. Es útil para encontrar información expuesta públicamente en la web.

## Instalación

Asegúrate de tener Python 3 instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

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
