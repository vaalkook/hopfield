FROM python:3.12-slim
WORKDIR /app

# Copiar solo los archivos que existen
COPY hopfield_numeros.py .
COPY main.py .
COPY utils.py .
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto (solo si tu main.py usa Flask)
EXPOSE 5000

# Comando por defecto
CMD ["python", "main.py"]
