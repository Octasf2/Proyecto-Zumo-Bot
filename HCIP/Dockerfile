FROM python:3.9

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar archivos al contenedor
COPY . .

# Exponer el puerto de FastAPI
EXPOSE 7860

# Comando para correr la app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]