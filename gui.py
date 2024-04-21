import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from medication_logic import recommend_medication  # Import the new recommendation function
  # Ensure this is correctly implemented

def create_connection():
    """Create and return a database connection."""
    return sqlite3.connect('medical_data.db')

def search_patient():
    """Searches for patient records and displays them in the GUI."""
    for i in tree.get_children():
        tree.delete(i)
    conn = create_connection()
    patient_name = name_entry.get().strip()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM patients WHERE Name COLLATE NOCASE LIKE ?", (f'%{patient_name}%',))
        records = cur.fetchall()
        for record in records:
            tree.insert("", tk.END, values=record)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def update_patient():
    """Updates patient records to append new medical conditions rather than replacing them."""
    conn = create_connection()
    cur = conn.cursor()
    try:
        patient_name = name_entry.get().strip()
        new_condition = value_entry.get().strip()

        # Fetch the current conditions
        cur.execute("SELECT MedicalCondition FROM patients WHERE Name=?", (patient_name,))
        result = cur.fetchone()
        if result:
            existing_conditions = result[0]
            if existing_conditions:  # Check if there are any existing conditions
                updated_conditions = existing_conditions + "; " + new_condition  # Append new condition
            else:
                updated_conditions = new_condition  # No existing conditions, just add new one
        else:
            updated_conditions = new_condition  # No record found, assume new entry

        # Update the database with the new or appended conditions
        cur.execute("UPDATE patients SET MedicalCondition=? WHERE Name=?", (updated_conditions, patient_name))
        conn.commit()

        # Use the rule-based system to provide medication recommendations
        recommended_medication = recommend_medication(new_condition)
        messagebox.showinfo("Medication Recommendation", f"Recommended medication for {new_condition}: {recommended_medication}")
        messagebox.showinfo("Success", "Patient record updated successfully.")
    except Exception as e:
        messagebox.showerror("Error", "Failed to update patient record: {}".format(e))
    finally:
        conn.close()

app = tk.Tk()
app.title("Patient Records System")
def remove_condition():
    """Removes a specified condition from a patient's record."""
    conn = create_connection()
    cur = conn.cursor()
    try:
        patient_name = name_entry.get().strip()
        condition_to_remove = condition_entry.get().strip()
        cur.execute("SELECT MedicalCondition FROM patients WHERE Name=?", (patient_name,))
        result = cur.fetchone()
        if result:
            conditions = result[0].split('; ')
            if condition_to_remove in conditions:
                conditions.remove(condition_to_remove)
                updated_conditions = '; '.join(conditions)
                cur.execute("UPDATE patients SET MedicalCondition=? WHERE Name=?", (updated_conditions, patient_name))
                conn.commit()
                messagebox.showinfo("Success", "Condition removed successfully.")
            else:
                messagebox.showinfo("Info", "Condition not found.")
        else:
            messagebox.showinfo("Info", "No record found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to remove condition: {e}")
    finally:
        conn.close()



frame = ttk.Frame(app)
frame.pack(pady=20)

tree = ttk.Treeview(frame, columns=("Name", "Age", "Gender", "BloodType", "MedicalCondition", "DateOfAdmission",
                                    "Doctor", "Hospital", "InsuranceProvider", "BillingAmount", "RoomNumber",
                                    "AdmissionType", "DischargeDate", "Medication", "TestResults"), show="headings")
tree.pack()

for col in tree["columns"]:
    tree.heading(col, text=col)

tk.Label(app, text="Enter Patient Name:").pack()
name_entry = tk.Entry(app)
name_entry.pack()

search_btn = tk.Button(app, text="Search Patient", command=search_patient)
search_btn.pack()

tk.Label(app, text="Attribute to Update:").pack()
attribute_entry = tk.Entry(app)
attribute_entry.pack()

tk.Label(app, text="New Value:").pack()
value_entry = tk.Entry(app)
value_entry.pack()

update_btn = tk.Button(app, text="Update Attribute", command=update_patient)
update_btn.pack()

tk.Label(app, text="Condition to Remove:").pack()
condition_entry = tk.Entry(app)
condition_entry.pack()

remove_btn = tk.Button(app, text="Remove Condition", command=remove_condition)
remove_btn.pack()

app.mainloop()
