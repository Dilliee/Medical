import sqlite3

def create_connection():
    """Create and return a database connection."""
    return sqlite3.connect('patients.db')

def search_patient(conn, patient_name):
    """Retrieve a patient's records from the database."""
    cur = conn.cursor()
    cur.execute("SELECT * FROM patients WHERE name=?", (patient_name,))
    return cur.fetchall()

def update_patient(conn, patient_name, illness):
    """Update a patient's record with a new illness."""
    cur = conn.cursor()
    cur.execute("UPDATE patients SET illness=? WHERE name=?", (illness, patient_name))
    conn.commit()
