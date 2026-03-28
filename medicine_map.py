# medicine_map.py
# Maps predicted disease to suggested medicines and precautions

MEDICINE_MAP = {
    "Flu": {
        "medicines": ["Paracetamol (500mg)", "Oseltamivir (Tamiflu)", "Cetirizine", "Cough Syrup"],
        "precautions": ["Rest well", "Stay hydrated", "Avoid contact with others", "Take steam inhalation"],
        "severity": "Mild-Moderate"
    },
    "Common Cold": {
        "medicines": ["Paracetamol (500mg)", "Cetirizine", "Nasal Decongestant", "Vitamin C"],
        "precautions": ["Drink warm fluids", "Rest", "Cover nose while sneezing", "Avoid cold food"],
        "severity": "Mild"
    },
    "Malaria": {
        "medicines": ["Chloroquine", "Artemisinin-based therapy", "Primaquine", "Paracetamol"],
        "precautions": ["Use mosquito nets", "Apply mosquito repellent", "Consult doctor immediately", "Complete full course"],
        "severity": "Severe - See Doctor"
    },
    "Typhoid": {
        "medicines": ["Ciprofloxacin", "Azithromycin", "Ceftriaxone", "ORS Salts"],
        "precautions": ["Drink boiled water", "Eat light food", "Complete antibiotic course", "Bed rest"],
        "severity": "Moderate-Severe - See Doctor"
    },
    "Dengue": {
        "medicines": ["Paracetamol (for fever)", "ORS Salts", "Platelet boosting foods", "Papaya leaf extract"],
        "precautions": ["NO Aspirin or Ibuprofen", "Stay hydrated", "Monitor platelet count", "Hospitalize if severe"],
        "severity": "Severe - See Doctor"
    },
    "Diabetes": {
        "medicines": ["Metformin", "Insulin (if Type 1)", "Glipizide", "Sitagliptin"],
        "precautions": ["Monitor blood sugar daily", "Low sugar diet", "Regular exercise", "Regular doctor visits"],
        "severity": "Chronic - Ongoing Management"
    },
    "Hypertension": {
        "medicines": ["Amlodipine", "Lisinopril", "Losartan", "Hydrochlorothiazide"],
        "precautions": ["Reduce salt intake", "Exercise regularly", "Avoid stress", "Monitor BP daily"],
        "severity": "Chronic - Ongoing Management"
    },
    "Asthma": {
        "medicines": ["Salbutamol Inhaler", "Budesonide Inhaler", "Montelukast", "Prednisolone (for attacks)"],
        "precautions": ["Avoid triggers (dust, smoke)", "Keep inhaler handy", "Avoid cold air", "Regular checkups"],
        "severity": "Chronic - Ongoing Management"
    },
    "Pneumonia": {
        "medicines": ["Amoxicillin", "Azithromycin", "Levofloxacin", "Paracetamol"],
        "precautions": ["Complete antibiotic course", "Rest", "Stay warm", "Seek hospital care if breathing worsens"],
        "severity": "Moderate-Severe - See Doctor"
    },
    "COVID-19": {
        "medicines": ["Paracetamol", "Vitamin C & D", "Zinc supplements", "Favipiravir (if prescribed)"],
        "precautions": ["Isolate immediately", "Monitor oxygen levels", "Stay hydrated", "Seek hospital if O2 < 94%"],
        "severity": "Moderate-Severe - See Doctor"
    },
    "Gastritis": {
        "medicines": ["Omeprazole", "Pantoprazole", "Antacids (Gelusil)", "Domperidone"],
        "precautions": ["Avoid spicy food", "Eat small meals", "Avoid alcohol", "Don't skip meals"],
        "severity": "Mild-Moderate"
    },
    "Migraine": {
        "medicines": ["Ibuprofen", "Sumatriptan", "Naproxen", "Amitriptyline (preventive)"],
        "precautions": ["Rest in dark quiet room", "Avoid screen time", "Stay hydrated", "Identify triggers"],
        "severity": "Moderate"
    },
    "Anemia": {
        "medicines": ["Iron Supplements (Ferrous Sulphate)", "Folic Acid", "Vitamin B12", "Vitamin C"],
        "precautions": ["Eat iron-rich foods (spinach, meat)", "Avoid tea with meals", "Regular blood tests", "Consult doctor"],
        "severity": "Mild-Moderate"
    }
}

def get_medicine_info(disease_name):
    """Returns medicine and precaution info for a given disease."""
    return MEDICINE_MAP.get(disease_name, {
        "medicines": ["Please consult a doctor"],
        "precautions": ["Seek professional medical advice"],
        "severity": "Unknown"
    })