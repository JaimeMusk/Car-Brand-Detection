Car Brand Detection 🚗🔍
Descripción del proyecto
El proyecto Car Brand Detection busca detectar la marca y el modelo de un coche a partir de una imagen, utilizando un modelo de aprendizaje profundo. Este modelo está entrenado para reconocer distintas marcas y modelos y proporcionar un porcentaje de confianza en sus predicciones.

Este proyecto es el resultado de un esfuerzo por aplicar técnicas de inteligencia artificial y aprendizaje profundo a un problema del mundo real: la identificación automática de coches. Ha sido desarrollado como parte de un ejercicio académico.

Objetivo del proyecto
El objetivo principal fue diseñar, entrenar y desplegar un modelo de inteligencia artificial que permita identificar la marca y el modelo de un coche desde una imagen.

Lo que intentamos:
Investigar y analizar distintas técnicas de visión por computadora y redes neuronales.
Probar diferentes arquitecturas de modelos para obtener un modelo final que sea preciso y eficiente.
Crear una aplicación interactiva para que el modelo pueda ser utilizado fácilmente por los usuarios.
Lo que logramos:
Modelo final: Un modelo basado en redes neuronales convolucionales (CNN) entrenado para clasificar coches en
varias marcas y modelos populares con una precisión razonable. 2. Interfaz interactiva: Una aplicación basada en Gradio que permite a los usuarios subir imágenes y obtener predicciones inmediatas. 3. Despliegue con Docker: Una solución portable que permite ejecutar el proyecto en cualquier máquina con Docker instalado.

Cómo funciona
El sistema funciona de la siguiente manera:

Carga de imágenes: El usuario sube una imagen de un coche a través de la interfaz Gradio.
Preprocesamiento: La imagen es redimensionada a 224x224 píxeles y normalizada para que sea compatible con el modelo.
Predicción: El modelo procesará la imagen y determinará la marca y el modelo del coche con un porcentaje de confianza.
Resultado: La aplicación muestra el nombre del coche y el porcentaje de confianza calculado.
Requisitos para usar el proyecto
Software necesario:
Python 3.9 o superior
Docker
Bibliotecas necesarias: TensorFlow, Gradio, NumPy, Pillow
Instrucciones para ejecutar el proyecto
1. Clonar el repositorio
bash
Copy code
git clone https://github.com/JaimeMusk/Car-Brand-Detection.git
cd Car-Brand-Detection
2. Construir la imagen de Docker
bash
Copy code
docker build -t car-brand-detector .
3. Ejecutar el contenedor
bash
Copy code
docker run -p 8080:8080 car-brand-detector
4. Abrir la aplicación
Abre tu navegador y accede a:

arduino
Copy code
http://127.0.0.1:8080
Cómo usamos la IA
El modelo utilizado es una red neuronal convolucional (CNN) entrenada específicamente para reconocer imágenes de coches. Este modelo fue entrenado utilizando un conjunto de datos de imágenes etiquetadas que contienen múltiples marcas y modelos de coches.

Arquitectura: CNN con capas convolucionales, de pooling y densas.
Entrenamiento: Dataset balanceado con imágenes de distintas marcas/modelos.
Salida: Predicción de la marca y modelo del coche con la mayor probabilidad.
Ejemplo de uso
Sube una imagen de un coche en la interfaz.
Obtén el resultado, por ejemplo:
Imagen subida: Foto de un Lamborghini Gallardo.
Resultado: Lamborghini Gallardo LP 570-4 Superleggera 2012 (Confianza: 93.6%).
Autores
Jaime Ortueta
