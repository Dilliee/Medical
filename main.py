from data_preprocessing import preprocess_data
from eda import perform_eda
from model import train_and_evaluate_model

def main():
    filepath = r'C:\Users\Admin\Documents\Spreadsheets\Medical.csv'  # Use raw string for the path
    data = preprocess_data(filepath)
    if 'Outcome' in data.columns:
        perform_eda(data)
        model = train_and_evaluate_model(data, 'Outcome')
    else:
        print("Outcome column is missing from the data.")

if __name__ == "__main__":
    main()
