import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import pickle


def preprocess_data(data):
    """Preprocesses the data by filling missing values and scaling numerical features."""
    # Handling missing values
    data.fillna(data.mean(), inplace=True)

    # Scaling numeric features
    numeric_cols = data.select_dtypes(include=['number']).columns
    scaler = StandardScaler()
    data[numeric_cols] = scaler.fit_transform(data[numeric_cols])

    return data, scaler


def train_model(data_path):
    """Trains a Random Forest model on data from the specified CSV file."""
    # Load and preprocess data
    data = pd.read_csv(data_path)
    X = data.drop('Medication', axis=1)  # Assuming 'Medication' is the target column
    y = data['Medication']

    X, scaler = preprocess_data(X)

    # Splitting data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Training the RandomForest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Saving the model and scaler to files
    with open('medication_model.pkl', 'wb') as model_file, open('scaler.pkl', 'wb') as scaler_file:
        pickle.dump(model, model_file)
        pickle.dump(scaler, scaler_file)

    print("Model and scaler saved to 'medication_model.pkl' and 'scaler.pkl'.")


if __name__ == "__main__":
    # Replace 'path_to_your_data.csv' with the actual path to your dataset
    train_model('path_to_your_data.csv')
