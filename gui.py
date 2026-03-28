# gui.py
# Run this AFTER train_model.py
# Command: python gui.py

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import pickle
import os
import sys
import numpy as np

# ── Make sure medicine_map.py can be found (same folder) ──
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medicine_map import get_medicine_info

# ─────────────────────────────────────────────
# Load saved model, encoder, symptoms list
# ─────────────────────────────────────────────
def load_model():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(base_dir, "model.pkl"), "rb") as f:
            model = pickle.load(f)
        with open(os.path.join(base_dir, "label_encoder.pkl"), "rb") as f:
            le = pickle.load(f)
        with open(os.path.join(base_dir, "symptoms_list.pkl"), "rb") as f:
            symptoms = pickle.load(f)
        print("[✓] Model loaded successfully.")
        return model, le, symptoms
    except FileNotFoundError:
        messagebox.showerror(
            "Model Not Found",
            "model.pkl not found!\n\nPlease run train_model.py first:\n  python train_model.py"
        )
        return None, None, None

# ─────────────────────────────────────────────
# Predict disease from selected symptoms
# ─────────────────────────────────────────────
def predict_disease(selected_symptoms, model, le, all_symptoms):
    input_vector = [1 if s in selected_symptoms else 0 for s in all_symptoms]
    prediction = model.predict([input_vector])
    disease = le.inverse_transform(prediction)[0]
    return disease

# ─────────────────────────────────────────────
# Main GUI Class
# ─────────────────────────────────────────────
class DiseasePredictorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Disease Predictor — CSA2001 VIT Bhopal")
        self.root.geometry("960x700")
        self.root.configure(bg="#f0f4f8")
        self.root.resizable(True, True)

        self.model, self.le, self.all_symptoms = load_model()
        if not self.model:
            return

        self.selected = set()
        self.symptom_vars = {}
        self._build_ui()

    def _build_ui(self):
        # ── Title Bar ──
        title_frame = tk.Frame(self.root, bg="#1a73e8", pady=14)
        title_frame.pack(fill="x")
        tk.Label(title_frame,
                 text="🩺  AI Disease Prediction System",
                 font=("Arial", 18, "bold"),
                 bg="#1a73e8", fg="white").pack()
        tk.Label(title_frame,
                 text="CSA2001 — Fundamentals of AI & ML  |  VIT Bhopal",
                 font=("Arial", 9),
                 bg="#1a73e8", fg="#cce0ff").pack()

        # ── Main 2-column layout ──
        main_frame = tk.Frame(self.root, bg="#f0f4f8")
        main_frame.pack(fill="both", expand=True, padx=15, pady=10)

        # ── LEFT: Symptom Panel ──
        left = tk.LabelFrame(main_frame,
                             text="  Select Symptoms  ",
                             font=("Arial", 11, "bold"),
                             bg="#f0f4f8", fg="#1a73e8",
                             padx=8, pady=8)
        left.pack(side="left", fill="both", expand=True, padx=(0, 8))

        # Search bar
        sf = tk.Frame(left, bg="#f0f4f8")
        sf.pack(fill="x", pady=(0, 6))
        tk.Label(sf, text="🔍 Search:", bg="#f0f4f8", font=("Arial", 9)).pack(side="left")
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self._filter_symptoms)
        tk.Entry(sf, textvariable=self.search_var,
                 font=("Arial", 10), width=22).pack(side="left", padx=5)
        tk.Button(sf, text="✕ Clear",
                  command=self._clear_search,
                  bg="#e8f0fe", font=("Arial", 8),
                  relief="flat").pack(side="left")

        # Scrollable checkbox area
        cf = tk.Frame(left, bg="#f0f4f8")
        cf.pack(fill="both", expand=True)
        self.canvas = tk.Canvas(cf, bg="#ffffff",
                                highlightthickness=1,
                                highlightbackground="#d0d8e4")
        sb = ttk.Scrollbar(cf, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.check_frame = tk.Frame(self.canvas, bg="#ffffff")
        self.canvas.create_window((0, 0), window=self.check_frame, anchor="nw")
        self.check_frame.bind("<Configure>", lambda e:
            self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Mouse scroll support
        self.canvas.bind("<Enter>", lambda e:
            self.canvas.bind_all("<MouseWheel>", self._on_mousewheel))
        self.canvas.bind("<Leave>", lambda e:
            self.canvas.unbind_all("<MouseWheel>"))

        self._render_checkboxes(self.all_symptoms)

        # Selected count
        self.count_label = tk.Label(left,
                                    text="Selected: 0 symptoms",
                                    bg="#f0f4f8",
                                    font=("Arial", 9, "italic"),
                                    fg="#555")
        self.count_label.pack(pady=(4, 0))

        # Action buttons
        btn_frame = tk.Frame(left, bg="#f0f4f8")
        btn_frame.pack(pady=8)
        tk.Button(btn_frame,
                  text="🔮  Predict Disease",
                  command=self._predict,
                  bg="#1a73e8", fg="white",
                  font=("Arial", 11, "bold"),
                  padx=16, pady=7,
                  relief="flat", cursor="hand2").pack(side="left", padx=5)
        tk.Button(btn_frame,
                  text="🔄  Reset",
                  command=self._reset,
                  bg="#ea4335", fg="white",
                  font=("Arial", 10),
                  padx=12, pady=7,
                  relief="flat", cursor="hand2").pack(side="left", padx=5)

        # ── RIGHT: Results Panel ──
        right = tk.LabelFrame(main_frame,
                              text="  Prediction Results  ",
                              font=("Arial", 11, "bold"),
                              bg="#f0f4f8", fg="#1a73e8",
                              padx=8, pady=8)
        right.pack(side="right", fill="both", expand=True)

        self.result_box = scrolledtext.ScrolledText(
            right,
            font=("Courier New", 10),
            bg="#1e1e1e", fg="#00ff88",
            wrap=tk.WORD,
            state="disabled",
            height=32)
        self.result_box.pack(fill="both", expand=True)
        self._show_welcome()

    # ── Render symptom checkboxes ──
    def _render_checkboxes(self, symptoms):
        for w in self.check_frame.winfo_children():
            w.destroy()
        self.symptom_vars = {}
        for i, symptom in enumerate(sorted(symptoms)):
            var = tk.BooleanVar(value=(symptom in self.selected))
            cb = tk.Checkbutton(
                self.check_frame,
                text=symptom.replace("_", " ").title(),
                variable=var,
                bg="#ffffff",
                activebackground="#e8f0fe",
                font=("Arial", 9),
                command=lambda s=symptom, v=var: self._toggle(s, v)
            )
            cb.grid(row=i, column=0, sticky="w", padx=8, pady=2)
            self.symptom_vars[symptom] = var

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _filter_symptoms(self, *args):
        q = self.search_var.get().lower().replace(" ", "_")
        filtered = [s for s in self.all_symptoms if q in s.lower()]
        self._render_checkboxes(filtered)

    def _clear_search(self):
        self.search_var.set("")
        self._render_checkboxes(self.all_symptoms)

    def _toggle(self, symptom, var):
        if var.get():
            self.selected.add(symptom)
        else:
            self.selected.discard(symptom)
        self.count_label.config(text=f"Selected: {len(self.selected)} symptoms")

    def _predict(self):
        if len(self.selected) < 2:
            messagebox.showwarning("Too Few Symptoms",
                                   "Please select at least 2 symptoms to predict.")
            return
        disease = predict_disease(self.selected, self.model, self.le, self.all_symptoms)
        info = get_medicine_info(disease)
        self._show_result(disease, info)

    def _show_result(self, disease, info):
        self.result_box.config(state="normal")
        self.result_box.delete("1.0", tk.END)

        lines = [
            "",
            "╔══════════════════════════════════════════╗",
            "║         PREDICTION RESULT                ║",
            "╚══════════════════════════════════════════╝",
            "",
            f"  🦠 PREDICTED DISEASE:",
            f"     {disease}",
            "",
            f"  ⚠  SEVERITY:",
            f"     {info['severity']}",
            "",
            "  💊 SUGGESTED MEDICINES:",
        ]
        for i, med in enumerate(info["medicines"], 1):
            lines.append(f"     {i}. {med}")
        lines += ["", "  ✅ PRECAUTIONS:"]
        for i, p in enumerate(info["precautions"], 1):
            lines.append(f"     {i}. {p}")
        lines += [
            "",
            "──────────────────────────────────────────",
            "  ⚕ DISCLAIMER:",
            "    This is an AI prediction only.",
            "    Always consult a qualified doctor.",
            "──────────────────────────────────────────",
            "",
            f"  Symptoms selected ({len(self.selected)}):",
            f"  {', '.join(sorted(self.selected))}",
            "",
        ]
        self.result_box.insert(tk.END, "\n".join(lines))
        self.result_box.config(state="disabled")

    def _show_welcome(self):
        self.result_box.config(state="normal")
        self.result_box.insert(tk.END, """
╔══════════════════════════════════════════╗
║    Welcome to AI Disease Predictor       ║
║    CSA2001 — VIT Bhopal                  ║
╚══════════════════════════════════════════╝

  HOW TO USE:
  ─────────────────────────────────────────
   1. Search or scroll the symptom list
   2. Tick all symptoms you are feeling
   3. Click  🔮 Predict Disease
   4. See disease + medicines on the right

  ML MODELS USED (as per syllabus CO4):
   • Decision Tree
   • Random Forest  (Ensemble Method)
   • Naive Bayes    (Probabilistic, CO3)

  Best model is auto-selected by accuracy.

  ─────────────────────────────────────────
  ⚕ For educational purposes only.
    Always consult a real doctor.
  ─────────────────────────────────────────
""")
        self.result_box.config(state="disabled")

    def _reset(self):
        self.selected.clear()
        self.search_var.set("")
        self._render_checkboxes(self.all_symptoms)
        self.count_label.config(text="Selected: 0 symptoms")
        self.result_box.config(state="normal")
        self.result_box.delete("1.0", tk.END)
        self._show_welcome()


# ─────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = DiseasePredictorApp(root)
    root.mainloop()