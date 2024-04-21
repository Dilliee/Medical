import pandas as pd


def load_data(filepath):
    """Load CSV data from a given file path."""
    try:
        data = pd.read_csv(filepath)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print("File not found. Please check the filepath.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def clean_data(data):
    """Clean data by filling missing values and removing outliers."""
    if data is not None:
        # Fill missing numeric values with the mean
        for col in data.select_dtypes(include=['number']).columns:
            data.loc[:, col] = data.loc[:, col].fillna(data[col].mean())

        print("Data cleaning completed.")
        return data
    else:
        print("No data to clean.")
        return None


def add_features(data):
    """Add or transform features."""
    if data is not None:
        if 'Age' in data.columns and 'Test Results' in data.columns:
            # Example transformation (customize as needed)
            data['AgeNormalized'] = data['Age'] / data['Age'].max()
            print("Features added/transformed.")
        else:
            print("Required columns are missing for feature transformation.")
        return data
    else:
        print("No data to process.")
        return None

def add_outcome_feature(data):
    """Create an Outcome feature based on Test Results or other logic."""
    if 'Test Results' in data.columns:
        data['Outcome'] = (data['Test Results'] == 'Normal').astype(int)
        print("Outcome feature added.")
    else:
        print("Test Results column not found.")
    return data



def preprocess_data(filepath):
    data = load_data(filepath)
    data = clean_data(data)
    data = add_features(data)
    data = add_outcome_feature(data)
    print("Columns after preprocessing:", data.columns)
    return data




if __name__ == "__main__":
    filepath = r'C:\Users\Admin\Documents\Spreadsheets\Medical.csv'  # Use raw string for the path
    processed_data = preprocess_data(filepath)
    if processed_data is not None:
        print(processed_data.head())  # Print first few rows to check the processed data
    else:
        print("Failed to process data.")
