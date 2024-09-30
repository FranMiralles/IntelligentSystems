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


def loadData(test_size=0.2, random_state=42):
    digits = load_digits()
    X = digits.data
    y = digits.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test


def trainDecisionTree(X_train, X_test, y_train, y_test, random_state=42):
    dt_model = DecisionTreeClassifier(random_state=random_state)
    dt_model.fit(X_train, y_train)
    y_pred_dt = dt_model.predict(X_test)
    print(f"Accuracy Decision Tree: {accuracy_score(y_test, y_pred_dt)}")
    return dt_model


def trainRandomForest(X_train, X_test, y_train, y_test, random_state=42, n_estimators=100):
    rf_model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
    rf_model.fit(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)
    print(f"Accuracy Random Forest: {accuracy_score(y_test, y_pred_rf)}")
    return rf_model

def trainBagging(X_train, X_test, y_train, y_test, random_state=42, n_estimators=50):
    bg_model = BaggingClassifier(base_estimator=DecisionTreeClassifier(), n_estimators=n_estimators, random_state=random_state)
    bg_model.fit(X_train, y_train)
    y_pred_bg = bg_model.predict(X_test)
    print(f'Accuracy Bagging: {accuracy_score(y_test, y_pred_bg)}')
    return bg_model

def trainAdaboost(X_train, X_test, y_train, y_test, random_state=42, n_estimators=50):
    ab_model = AdaBoostClassifier(n_estimators=n_estimators, random_state=random_state)
    ab_model.fit(X_train, y_train)
    y_pred_ab = ab_model.predict(X_test)
    print(f'Accuracy AdaBoost: {accuracy_score(y_test, y_pred_ab)}')
    return ab_model

def trainGradientBoosting(X_train, X_test, y_train, y_test, random_state=42, n_estimators=50):
    gd_model = GradientBoostingClassifier(n_estimators=n_estimators, random_state=random_state)
    gd_model.fit(X_train, y_train)
    y_pred_gb = gd_model.predict(X_test)
    print(f'Accuracy Gradient Boosting: {accuracy_score(y_test, y_pred_gb)}')
    return gd_model


def storeDecisionTree(dt_model):
    joblib.dump(dt_model, os.path.join(MODELS_DIR, 'decision_tree.joblib')) # fileName
    return True

def storeRandomForest(rf_model):
    joblib.dump(rf_model, os.path.join(MODELS_DIR, 'random_forest.joblib')) # fileName
    return True


def processDecisionTree(test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = loadData(test_size=test_size, random_state=random_state)
    dt_model = trainDecisionTree(X_train, X_test, y_train, y_test, random_state=random_state)
    return storeDecisionTree(dt_model=dt_model)

def processRandomForest(test_size=0.2, random_state=42, n_estimators=100):
    X_train, X_test, y_train, y_test = loadData(test_size=test_size, random_state=random_state)
    rf_model = trainRandomForest(X_train, X_test, y_train, y_test, random_state=random_state, n_estimators=n_estimators)
    return storeRandomForest(rf_model=rf_model)

def predictFromDecisionTree(imageToPredict):
    dt_model = joblib.load(os.path.join(MODELS_DIR, 'decision_tree.joblib'))
    if isinstance(dt_model, DecisionTreeClassifier):
        image_vector = imageToPredict.flatten().reshape(1, -1)
        return int(dt_model.predict(image_vector)[0])
    else:
        return -1

def predictFromRandomForest(imageToPredict):
    rf_model = joblib.load(os.path.join(MODELS_DIR, 'random_forest.joblib'))
    if isinstance(rf_model, RandomForestClassifier):
        image_vector = imageToPredict.flatten().reshape(1, -1)
        return int(rf_model.predict(image_vector)[0])
    else:
        return -1


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