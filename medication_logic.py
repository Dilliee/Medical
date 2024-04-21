# medication_logic.py
# This file now handles medication recommendations using a rule-based system.

def recommend_medication(condition):
    """
    Returns a recommended medication based on the provided condition using a rule-based system.
    """
    recommendations = {
        "hypertension": "Amlodipine",
        "diabetes": "Metformin",
        "high cholesterol": "Atorvastatin",
        "cold": "Cough Syrup",
        "allergy": "Antihistamines",
        "headache": "Ibuprofen",
        "asthma": "Inhale corticosteroids",
        "depression": "Fluoxetine",
        "type 1 diabetes": "Insulin",
        "type 2 diabetes": "Metformin",
        "common cold": "Cough Syrup",
        "seasonal allergy": "Cetirizine",
        "acid reflux": "Omeprazole",
        "stomach ulcer": "Ranitidine",
        "anxiety": "Sertraline",
        "insomnia": "Zolpidem",
        "pain relief": "Acetaminophen",
        "arthritis": "Naproxen"
        # Add more conditions and their corresponding medications as needed
    }
    # Convert condition to lowercase to match dictionary keys
    medication = recommendations.get(condition.lower(), "Consult a specialist")
    return medication

# Example usage of the function
if __name__ == "__main__":
    # Testing the function with a sample condition
    print(recommend_medication("Hypertension"))
