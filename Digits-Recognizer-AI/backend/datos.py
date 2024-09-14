import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from PIL import Image

# Cargar el conjunto de datos de dígitos
digits = load_digits()

# Obtener los datos y las etiquetas
X = digits.data
y = digits.target

# Crear una figura con 10 subplots
fig, axes = plt.subplots(1, 10, figsize=(15, 5))

# Dibujar los primeros 10 dígitos
for i in range(10):
    # Convertir cada vector plano en una imagen 8x8
    image = X[i].reshape(8, 8)
    # Convertir el array a una imagen PIL
    image = Image.fromarray(image.astype(np.uint8))
    resized_image = image.resize((300, 300), Image.ANTIALIAS)
    
    # Mostrar la imagen en el subplot correspondiente
    axes[i].imshow(resized_image, cmap='gray', interpolation='nearest')
    axes[i].set_title(f'Label: {y[i]}')
    axes[i].axis('off')  # Desactivar los ejes

# Ajustar el layout para que no se solapen las imágenes
plt.tight_layout()
plt.show()