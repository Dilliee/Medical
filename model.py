from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, roc_auc_score
import numpy as np

def build_model():
    model = RandomForestClassifier(random_state=42)
    return model

def perform_grid_search(X_train, y_train):
    # Define the parameter grid to search
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_features': ['auto', 'sqrt', 'log2'],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }
    grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=42),
                               param_grid=param_grid,
                               cv=3,
                               verbose=2,
                               scoring='accuracy',
                               n_jobs=-1)
    grid_search.fit(X_train, y_train)
    print("Best parameters:", grid_search.best_params_)
    return grid_search.best_estimator_

def train_and_evaluate_model(data, target_column):
    if target_column not in data.columns:
        print(f"Error: Target column '{target_column}' not found in data.")
        return None  # Or raise an exception or handle the error as needed

    X = data.drop(target_column, axis=1)
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = perform_grid_search(X_train, y_train)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    prediction_probs = model.predict_proba(X_test)[:, 1]

    print(classification_report(y_test, predictions))
    print("Accuracy:", accuracy_score(y_test, predictions))
    print("ROC AUC:", roc_auc_score(y_test, prediction_probs))

    return model
