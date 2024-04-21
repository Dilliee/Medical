import pandas as pd
import sqlite3


def import_data_to_db(file_path, db_path='medical_data.db'):
    conn = sqlite3.connect(db_path)
    data = pd.read_csv(file_path)

    # Rename columns to match the database schema
    data.columns = [col.replace(" ", "") for col in data.columns]  # Removing spaces or replace with underscore
    data.to_sql('patients', conn, if_exists='append', index=False)

    print("Data imported successfully.")
    conn.close()


if __name__ == "__main__":
    import_data_to_db(r'C:\Users\Admin\Documents\Spreadsheets\Medical.csv')
