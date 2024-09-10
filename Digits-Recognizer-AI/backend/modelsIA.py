from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

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


def storeDecisionTree(dt_model):
    model_dir = '/models/'
    joblib.dump(dt_model, os.path.join(MODELS_DIR, 'decision_tree.joblib'))
    return True

def storeRandomForest(rf_model):
    model_dir = '/models'
    joblib.dump(rf_model, os.path.join(MODELS_DIR, 'random_forest.joblib'))
    return True


def processDecisionTree(test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = loadData(test_size=test_size, random_state=random_state)
    dt_model = trainDecisionTree(X_train, X_test, y_train, y_test, random_state=random_state)
    return storeDecisionTree(dt_model=dt_model)

def processRandomForest(test_size=0.2, random_state=42, n_estimators=100):
    X_train, X_test, y_train, y_test = loadData(test_size=test_size, random_state=random_state)
    rf_model = trainRandomForest(X_train, X_test, y_train, y_test, random_state=random_state, n_estimators=n_estimators)
    return storeRandomForest(rf_model=rf_model)

processDecisionTree(0.2, 42)
processRandomForest(0.2, 20, 200)