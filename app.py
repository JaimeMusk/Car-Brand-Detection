import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image
import os

# Desactivar la GPU
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


# Cargar el modelo entrenado
model = tf.keras.models.load_model("modelo_final_test.keras")

# Clases disponibles
classes = [
    "Bugatti Veyron 16.4 Coupe 2009",
    "BMW M6 Convertible 2010",
    "Mercedes-Benz E-Class Sedan 2012",
    "Chevrolet Corvette Ron Fellows Edition Z06 2007",
    "Chevrolet Corvette Convertible 2012",
    "Lamborghini Gallardo LP 570-4 Superleggera 2012",
    "Lamborghini Aventador Coupe 2012",
    "Lamborghini Reventon Coupe 2008"
]

# Función para predecir
def predict_car(image):
    img = Image.fromarray(image).resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    class_idx = np.argmax(predictions)
    confidence = predictions[0][class_idx] * 100
    return f"Marca predicha: {classes[class_idx]} (Confianza: {confidence:.2f}%)"

# Interfaz de Gradio
interface = gr.Interface(
    fn=predict_car,
    inputs=gr.Image(type="numpy", label="Sube una imagen del coche"),
    outputs=gr.Textbox(label="Predicción")
)

# Lanzar la aplicación
interface.launch(server_name="0.0.0.0", server_port=8080)

