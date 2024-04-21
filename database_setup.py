import sqlite3


def create_db_and_table():
    conn = sqlite3.connect('medical_data.db')  # This creates the database file
    c = conn.cursor()

    # Drop the old table if needed (uncomment the next line if resetting the table is required)
    # c.execute('DROP TABLE IF EXISTS patients')

    # Create table with corrected column names, ensuring no inline SQL comments
    c.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            Name TEXT,
            Age INTEGER,
            Gender TEXT,
            BloodType TEXT,
            MedicalCondition TEXT,
            DateOfAdmission TEXT,
            Doctor TEXT,
            Hospital TEXT,
            InsuranceProvider TEXT,
            BillingAmount REAL,
            RoomNumber INTEGER,
            AdmissionType TEXT,
            DischargeDate TEXT,
            Medication TEXT,
            TestResults TEXT
        )
    ''')
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_db_and_table()
