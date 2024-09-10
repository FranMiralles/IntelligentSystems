from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

def loadData(test_size=0.2, random_state=42):
    digits = load_digits()
    X = digits.data
    y = digits.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

def trainDecisionTree(X_train, X_test, y_train, y_test):
    dt_model = DecisionTreeClassifier(random_state=42)
    dt_model.fit(X_train, y_train)
    y_pred_dt = dt_model.predict(X_test)
    print(f"Accuracy Decision Tree: {accuracy_score(y_test, y_pred_dt)}")
    return dt_model



def trainRandomForest(X_train, X_test, y_train, y_test):
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)
    print(f"Accuracy Random Forest: {accuracy_score(y_test, y_pred_rf)}")
    return rf_model

def storeDecisionTree():
    model_dir = './models'

    joblib.dump(dt_model, os.path.join(model_dir, 'decision_tree.joblib'))
    joblib.dump(rf_model, os.path.join(model_dir, 'random_forest.joblib'))