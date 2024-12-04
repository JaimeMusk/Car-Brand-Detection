# Usar la imagen base de Python con las herramientas necesarias
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo app.py y el modelo al contenedor
COPY app.py /app/app.py
COPY modelo_final_test.keras /app/modelo_final_test.keras

# Instalar las dependencias necesarias
RUN pip install --no-cache-dir tensorflow gradio pillow numpy

# Exponer el puerto que usará la aplicación
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
