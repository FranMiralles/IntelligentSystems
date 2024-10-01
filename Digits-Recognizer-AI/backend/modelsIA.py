from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier, BaggingClassifier, GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(SCRIPT_DIR, 'models')
DECISION_TREE_FILE = os.path.join(MODELS_DIR, 'decision_tree.joblib')
RANDOM_FOREST_FILE = os.path.join(MODELS_DIR, 'random_forest.joblib')
BAGGING_FILE = os.path.join(MODELS_DIR, 'bagging.joblib')
ADABOOST_FILE = os.path.join(MODELS_DIR, 'adaboost.joblib')
GRADIENT_BOOSTING_FILE = os.path.join(MODELS_DIR, 'gradient_boosting.joblib')
DECISION_TREE_MODEL = "decision_tree"
RANDOM_FOREST_MODEL = "decision_tree"
BAGGING_MODEL = "bagging"
ADABOOST_MODEL = "adaboost"
GRADIENT_BOOSTING_MODEL = "gradient_boosting"


def loadData(test_size=0.2, random_state=42):
    digits = load_digits()
    X = digits.data
    y = digits.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test


def trainModel(modelName, test_size=0.2, random_state=42, n_estimators=100):
    X_train, X_test, y_train, y_test = loadData(test_size=test_size, random_state=random_state)

    # Instantiate model
    if modelName == DECISION_TREE_MODEL:
        model = DecisionTreeClassifier(random_state=random_state)
        fileToStore = DECISION_TREE_FILE
    if modelName == RANDOM_FOREST_MODEL:
        model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
        fileToStore = RANDOM_FOREST_FILE
    if modelName == BAGGING_MODEL:
        model = BaggingClassifier(estimator=DecisionTreeClassifier(), n_estimators=n_estimators, random_state=random_state)
        fileToStore = BAGGING_FILE
    if modelName == ADABOOST_MODEL:
        model = AdaBoostClassifier(estimator=DecisionTreeClassifier(), algorithm='SAMME', n_estimators=n_estimators, random_state=random_state)
        fileToStore = ADABOOST_FILE
    if modelName == GRADIENT_BOOSTING_MODEL:
        model = GradientBoostingClassifier(n_estimators=n_estimators, random_state=random_state)
        fileToStore = GRADIENT_BOOSTING_FILE


    model.fit(X_train, y_train)
    # Store model
    joblib.dump(model, fileToStore)
    y_pred_dt = model.predict(X_test)
    return accuracy_score(y_test, y_pred_dt)


def predictFromModel(modelFile, imageToPredict):
    model = joblib.load(modelFile)
    image_vector = imageToPredict.flatten().reshape(1, -1)
    return int(model.predict(image_vector)[0])


def base64_to_grayscale_array(image_base64):
    # Decodificar la imagen en base64
    image_data = base64.b64decode(image_base64.split(',')[1])
    
    # Convertir los datos en un objeto PIL Image
    image = Image.open(BytesIO(image_data))
    
    # Convertir la imagen a escala de grises
    grayscale_image = image.convert("L")
    
    # Convertir la imagen a un array de numpy
    grayscale_array = np.array(grayscale_image)
    
    # Escalar los valores de los píxeles de 0 a 16
    scaled_grayscale_array = np.round((grayscale_array / 255) * 16).astype(int)
    adjusted_grayscale_array = np.abs(scaled_grayscale_array - 16)

    
    return adjusted_grayscale_array

def resize_image_to_8x8(grayscale_array):
    # Convertir el array a una imagen PIL
    image = Image.fromarray(grayscale_array.astype(np.uint8))
    
    # Redimensionar la imagen a 8x8 píxeles
    resized_image = image.resize((8, 8), Image.Resampling.LANCZOS)
    
    # Convertir la imagen redimensionada a un array
    return np.array(resized_image)

def display_image(image_array):
    plt.imshow(image_array, cmap='gray', vmin=0, vmax=16)
    plt.colorbar(label='Escala de Grises (0-16)')
    plt.show()


# processDecisionTree(0.2, 42)
# processRandomForest(0.2, 20, 200)