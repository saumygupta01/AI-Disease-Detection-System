# train_model.py
# Run this FIRST to train the ML model
# Command: python train_model.py

import pandas as pd
import numpy as np
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# ─────────────────────────────────────────────
# Step 1: Load Dataset
# ─────────────────────────────────────────────
def load_data():
    # Always look in the same folder as this script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "disease_symptoms.csv")

    if not os.path.exists(data_path):
        raise FileNotFoundError(
            f"\n[ERROR] disease_symptoms.csv not found!\n"
            f"Please place disease_symptoms.csv in:\n  {base_dir}\n"
        )

    df = pd.read_csv(data_path)
    print(f"[✓] Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

# ─────────────────────────────────────────────
# Step 2: Preprocess Data
# ─────────────────────────────────────────────
def preprocess(df):
    symptom_cols = [col for col in df.columns if col.startswith("Symptom")]

    # Collect all unique symptoms
    all_symptoms = set()
    for col in symptom_cols:
        all_symptoms.update(df[col].dropna().str.strip().unique())
    all_symptoms = sorted(list(all_symptoms))

    # Binary encode: 1 = symptom present, 0 = absent
    X = pd.DataFrame(0, index=df.index, columns=all_symptoms)
    for col in symptom_cols:
        for idx, val in df[col].dropna().items():
            val = val.strip()
            if val in X.columns:
                X.at[idx, val] = 1

    # Encode disease labels to numbers
    le = LabelEncoder()
    y = le.fit_transform(df["Disease"])

    print(f"[✓] Total unique symptoms (features): {len(all_symptoms)}")
    print(f"[✓] Total unique diseases (classes):  {len(le.classes_)}")
    print(f"[✓] Diseases: {list(le.classes_)}")
    return X, y, le, all_symptoms

# ─────────────────────────────────────────────
# Step 3: Train & Compare 3 Models
# ─────────────────────────────────────────────
def train_and_evaluate(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    models = {
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "Naive Bayes":   GaussianNB()
    }

    print("\n" + "="*50)
    print("     MODEL COMPARISON  (CSA2001 Project)")
    print("="*50)

    best_model = None
    best_accuracy = 0
    best_name = ""

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"  {name:20s} → Accuracy: {acc*100:.2f}%")
        if acc > best_accuracy:
            best_accuracy = acc
            best_model = model
            best_name = name

    print("="*50)
    print(f"  Best Model Selected: {best_name} ({best_accuracy*100:.2f}%)")
    print("="*50)
    return best_model, best_name

# ─────────────────────────────────────────────
# Step 4: Save Model (same folder as script)
# ─────────────────────────────────────────────
def save_model(model, le, all_symptoms):
    base_dir = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(base_dir, "model.pkl"), "wb") as f:
        pickle.dump(model, f)
    with open(os.path.join(base_dir, "label_encoder.pkl"), "wb") as f:
        pickle.dump(le, f)
    with open(os.path.join(base_dir, "symptoms_list.pkl"), "wb") as f:
        pickle.dump(all_symptoms, f)

    print(f"\n[✓] Saved: model.pkl")
    print(f"[✓] Saved: label_encoder.pkl")
    print(f"[✓] Saved: symptoms_list.pkl")
    print(f"[✓] All files saved in: {base_dir}")

# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("\n===== AI Disease Predictor — Training =====\n")
    df = load_data()
    X, y, le, all_symptoms = preprocess(df)
    best_model, best_name = train_and_evaluate(X, y)
    save_model(best_model, le, all_symptoms)
    print(f"\n[✓] Done! Now run: python gui.py\n")