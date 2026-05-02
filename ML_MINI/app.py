import tkinter as tk
import customtkinter as ctk
import pickle
import pandas as pd
import os

# --- Configuration ---
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue") 

# Load model logic
def load_assets():
    try:
        # Checking if files exist before loading to prevent crashes
        model_path = "model/model.pkl"
        le_path = "model/label_encoder.pkl"
        
        if os.path.exists(model_path) and os.path.exists(le_path):
            model = pickle.load(open(model_path, "rb"))
            le = pickle.load(open(le_path, "rb"))
            return model, le
        else:
            return None, None
    except Exception as e:
        print(f"Error loading model: {e}")
        return None, None

model, le = load_assets()

def predict():
    if model is None or le is None:
        output_label.configure(text="Error: Model files missing", text_color="orange")
        return

    # Prepare data for prediction
    data = pd.DataFrame({
        'Contains_Link': [link_var.get()],
        'Contains_Attachment': [attach_var.get()],
        'Urgent_Words': [urgent_var.get()],
        'From_Trusted_Domain': [trusted_var.get()]
    })

    # Get prediction
    result = model.predict(data)
    label = le.inverse_transform(result)[0]

    # Visual updates based on result
    if label == "Phishing":
        result_card.configure(fg_color="#3d1a1a", border_color="#ff4d4d")
        output_label.configure(text="⚠️ PHISHING DETECTED", text_color="#ff4d4d")
    else:
        result_card.configure(fg_color="#1a3d21", border_color="#4dff88")
        output_label.configure(text="✅ LEGITIMATE EMAIL", text_color="#4dff88")

# --- GUI Setup ---
root = ctk.CTk()
root.title("PhishGuard AI")
root.geometry("450x550")

# Header Section
title_label = ctk.CTkLabel(root, text="PhishGuard AI", font=("Helvetica", 26, "bold"))
title_label.pack(pady=(30, 5))

subtitle_label = ctk.CTkLabel(root, text="Security Analysis Tool", font=("Helvetica", 14), text_color="gray")
subtitle_label.pack(pady=(0, 20))

# Input Container
input_frame = ctk.CTkFrame(root, corner_radius=15)
input_frame.pack(pady=10, padx=40, fill="both", expand=True)

# Variables
link_var = tk.IntVar()
attach_var = tk.IntVar()
urgent_var = tk.IntVar()
trusted_var = tk.IntVar()

# Checkbox Styling
# Note: We use anchor="w" in .pack() to align them left
cb_pady = 12
cb_font = ("Helvetica", 14)

ctk.CTkCheckBox(input_frame, text="Contains Hyperlinks", variable=link_var, font=cb_font).pack(pady=cb_pady, padx=30, anchor="w")
ctk.CTkCheckBox(input_frame, text="Has Attachments", variable=attach_var, font=cb_font).pack(pady=cb_pady, padx=30, anchor="w")
ctk.CTkCheckBox(input_frame, text="Urgent Language", variable=urgent_var, font=cb_font).pack(pady=cb_pady, padx=30, anchor="w")
ctk.CTkCheckBox(input_frame, text="Trusted Domain", variable=trusted_var, font=cb_font).pack(pady=cb_pady, padx=30, anchor="w")

# Action Button
predict_btn = ctk.CTkButton(root, text="Analyze Email", font=("Helvetica", 15, "bold"), 
                            height=45, corner_radius=10, command=predict)
predict_btn.pack(pady=25, padx=60, fill="x")

# Result Display Card
result_card = ctk.CTkFrame(root, height=70, corner_radius=12, border_width=2, fg_color="transparent")
result_card.pack(pady=(0, 40), padx=40, fill="x")
result_card.pack_propagate(False) 

output_label = ctk.CTkLabel(result_card, text="Ready for Scan", font=("Helvetica", 16, "bold"))
output_label.pack(expand=True)

root.mainloop()