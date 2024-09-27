# Usar una imagen base de Python FROM python:3.9-slim
FROM python:3.9-slim
# Establecer el directorio de trabajo WORKDIR /app
workdir /app
#Copiar los archivos necesarios COPY. /app
COPY . /app
# Instalar dependencias
RUN pip install flask redis
# Exponer el puerto 5000 EXPOSE 5000
EXPOSE 5000
# Comando para ejecutar la aplicación CMD ["python", "app.py"]
CMD ["python", "app.py"]