# AI-Disease-Detection-System
|<p>**🩺 AI Disease Prediction System**</p><p>Symptom-Based Disease Predictor with Medicine Suggestions</p><p>👤 Author: Saumy Gupta</p><p>🆔 Registration Number : 25BCE10981</p><p>🏫 VIT Bhopal University</p><p>📘 Course: CSA2001 — Fundamentals of AI and ML</p>|
| :-: |


# **1. Project Overview**
This project is a Machine Learning-based Disease Prediction System developed as part of the CSA2001 — Fundamentals of AI and ML course at VIT Bhopal. The system accepts symptoms as input from a Tkinter GUI and predicts the probable disease using trained classification models, then recommends relevant medicines and precautions.

|**Field**|**Details**|
| :- | :- |
|Course Code|CSA2001|
|Course Name|Fundamentals of AI and ML|
|University|VIT Bhopal University|
|Language|Python 3.x|
|Interface|Tkinter Desktop GUI (built into Python)|
|Total Diseases|13 Diseases|
|Total Symptoms|~51 Unique Symptoms|
|Models Trained|Decision Tree, Random Forest, Naive Bayes|

# **2. Course Outcome (CO) Mapping**
This project directly addresses the following Course Outcomes from the CSA2001 syllabus:

|**CO**|**CO Description**|**How This Project Addresses It**|
| :- | :- | :- |
|CO1|Explain AI/ML capabilities & limitations|We compare Decision Tree, Random Forest, and Naive Bayes — analyzing strengths and accuracy of each|
|CO3|Describe learning models & algorithms|Probability (Naive Bayes), Statistical Decision Theory, Bayesian Statistics applied in model training|
|CO4|Analyze and design using AI techniques|Supervised Classification: labeled dataset, binary encoding, training, evaluation pipeline (train\_test\_split, accuracy\_score)|
|CO5|Apply ML algorithms to real-world problems|Disease prediction from symptoms is a real-world healthcare classification problem with a desktop GUI|

# **3. Libraries & Modules Used**
Install required libraries with the command below. tkinter and pickle come built into Python — no extra install needed.

|**Library / Module**|**Purpose**|**Syllabus Link**|
| :- | :- | :- |
|pandas|Load, clean, and manipulate the CSV dataset|CO4 — Data Representations|
|numpy|Numerical arrays for input vector encoding|CO3 — Linear Algebra|
|scikit-learn|Train models: DecisionTree, RandomForest, NaiveBayes|CO4 — ML Basics|
|scikit-learn|train\_test\_split, accuracy\_score, LabelEncoder|CO4 — Estimators & Validation|
|pickle (built-in)|Save and reload the trained model to/from disk|CO5 — Apply ML|
|tkinter (built-in)|Desktop GUI — checkboxes, search, buttons, result panel|CO5 — Real-world app|
|os (built-in)|File path management across platforms|Utility|

**📦  Installation Command:**

pip install pandas numpy scikit-learn

# **4. Machine Learning Models**
Three classification models are trained and compared automatically. The best-performing model is saved and used in the GUI.

|**Model**|**Algorithm Type**|**CO Mapping**|**Why Used**|
| :- | :- | :- | :- |
|Decision Tree|Supervised Classification|CO4|Easy to explain; visualizable as a flowchart of if/else decisions|
|Random Forest|Ensemble (Supervised)|CO4|Higher accuracy; combines 100 Decision Trees and takes majority vote|
|Naive Bayes|Probabilistic Classifier|CO3, CO4|Based on Bayesian Statistics (CO3); fast and effective for symptom data|

**Key ML Concepts Demonstrated:**

- **Supervised Learning —** labeled disease-symptom training data
- **Binary Feature Encoding —** 1 = symptom present, 0 = absent
- **train\_test\_split —** 80% training, 20% testing
- **accuracy\_score —** model evaluation metric (CO4)
- **LabelEncoder —** converts disease names to integer labels

# **5. Project Folder Structure**
All files are kept in ONE flat folder for simplicity. No subfolders needed.

|**File**|**Description**|
| :- | :- |
|disease\_symptoms.csv|Dataset — 13 diseases, ~51 symptoms (39 rows)|
|train\_model.py|Trains 3 ML models, compares accuracy, saves best model|
|gui.py|Tkinter desktop GUI — symptom selection + prediction result|
|medicine\_map.py|Dictionary: disease name → medicines + precautions|
|model.pkl|Saved trained model (created after running train\_model.py)|
|label\_encoder.pkl|Saved LabelEncoder for decoding predictions|
|symptoms\_list.pkl|Saved ordered list of all symptom features|
|README.md|This documentation file|

# **6. Setup & Run Instructions**
## **Step 1 — Install Python & Libraries**
Make sure Python 3.8 or above is installed. Open Command Prompt and run:

pip install pandas numpy scikit-learn

## **Step 2 — Place All Files in One Folder**
Put all 4 files in the same folder (e.g. Downloads\Disease Prediction Project\):

- **disease\_symptoms.csv**
- **train\_model.py**
- **gui.py**
- **medicine\_map.py**

## **Step 3 — Train the ML Model (Run Once)**
Open Command Prompt, navigate to your folder and run:

cd "C:\Users\YourName\Downloads\Disease Prediction Project"

python train\_model.py

This prints accuracy of all 3 models and saves model.pkl, label\_encoder.pkl, and symptoms\_list.pkl in the same folder.

## **Step 4 — Launch the GUI**
python gui.py

The desktop window opens. Select your symptoms and click Predict Disease.

# **7. How the System Works (Pipeline)**

1. **Load Dataset:** Read disease\_symptoms.csv using pandas
1. **Preprocess:** Extract all unique symptoms → binary encode each row (1 = present, 0 = absent)
1. **Encode Labels:** LabelEncoder converts disease name strings to integer numbers
1. **Train/Test Split:** 80% data for training, 20% for testing using train\_test\_split
1. **Train 3 Models:** Decision Tree + Random Forest + Naive Bayes are all trained
1. **Evaluate:** accuracy\_score compared for all 3 → best model auto-selected
1. **Save Model:** pickle saves model.pkl, label\_encoder.pkl, symptoms\_list.pkl
1. **GUI Launch:** User selects symptoms via checkboxes in Tkinter window
1. **Predict:** Input vector fed to saved model → disease decoded via LabelEncoder
1. **Display Result:** Disease name + medicines + precautions shown in result panel

# **8. Diseases Covered & Medicines**
The system covers 13 common diseases with suggested medicines and precautions:

|**Disease**|**Severity**|**Key Medicines**|**Important Note**|
| :- | :- | :- | :- |
|Flu|Mild-Moderate|Paracetamol, Oseltamivir|Rest & hydration|
|Common Cold|Mild|Paracetamol, Cetirizine|Warm fluids|
|Malaria|Severe|Chloroquine, Artemisinin|See doctor immediately|
|Typhoid|Moderate-Severe|Ciprofloxacin, Azithromycin|Complete antibiotic course|
|Dengue|Severe|Paracetamol, ORS|NO Aspirin or Ibuprofen|
|Diabetes|Chronic|Metformin, Insulin|Ongoing management|
|Hypertension|Chronic|Amlodipine, Lisinopril|Monitor BP daily|
|Asthma|Chronic|Salbutamol Inhaler|Keep inhaler handy|
|Pneumonia|Moderate-Severe|Amoxicillin, Azithromycin|Complete full course|
|COVID-19|Moderate-Severe|Paracetamol, Vit C & D|Isolate immediately|
|Gastritis|Mild-Moderate|Omeprazole, Antacids|Avoid spicy food|
|Migraine|Moderate|Ibuprofen, Sumatriptan|Dark quiet room|
|Anemia|Mild-Moderate|Iron Supplements, Vit B12|Iron-rich diet|

# **9. Disclaimer**

|<p>**⚠  IMPORTANT MEDICAL DISCLAIMER**</p><p>This project is built purely for educational purposes as part of the CSA2001 course at VIT Bhopal. The disease predictions are based on a small training dataset and are NOT medically validated. Do NOT use this tool for actual medical diagnosis or treatment decisions. Always consult a qualified and licensed medical professional for any health concerns.</p>|
| :- |

# **10. References**
- **S. Russell and P. Norvig,** Artificial Intelligence: A Modern Approach, Prentice Hall, 3rd Edition, 2009  [Course Textbook]
- **Ethem Alpaydin,** Machine Learning: The New AI, MIT Press, 2016  [Course Textbook]
- **Scikit-learn Documentation —** https://scikit-learn.org
- **Pandas Documentation —** https://pandas.pydata.org
- **Kaggle —** Disease Symptom and Patient Profile Dataset
- **Python Tkinter Docs —** https://docs.python.org/3/library/tkinter.html
CSA2001 — Fundamentals of AI & ML  |  VIT Bhopal  |  Page 1
