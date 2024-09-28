# Utilizar una imagen base de Python
FROM python:3-alpine3.15

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar todos los archivos al contenedor
COPY . /app

# Instalar las dependencias necesarias
RUN pip install -r requirements.txt

# Exponer el puerto que utilizará Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD python ./app.py

