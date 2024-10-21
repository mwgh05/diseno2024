# Utilizar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instalar las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos los archivos de la aplicación al directorio de trabajo
COPY . .

# Exponer el puerto que utilizará Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]