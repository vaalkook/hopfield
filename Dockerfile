# Usamos una imagen base de Python
FROM python:3.12-slim

# Crear directorio de la app
WORKDIR /app

# Copiar los archivos al contenedor
COPY hopfield_numeros.py .
COPY utils.py .
COPY app.py .
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto que Flask usará
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]
