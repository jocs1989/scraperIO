# Usa la imagen base
FROM unclecode/crawl4ai

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar todos los archivos desde el directorio actual al contenedor
COPY . /app/

# Comando para ejecutar el archivo `main.py` cuando se arranque el contenedor
CMD ["python", "main.py"]
