import tkinter as tk
from tkinter import scrolledtext, messagebox
from ttkthemes import ThemedTk
from ttkbootstrap import Style
import pickle

# Load the trained spam detection model
try:
    with open("spam_model.pkl", "rb") as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    messagebox.showerror("Error", "Trained model not found! Run the notebook first.")
    exit()

# Function to predict spam
def predict_spam():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter a message to classify.")
        return
    
    prediction = model.predict([text])[0]
    if prediction == 1:
        result_label.config(text="🚨 IT'S SPAM MAIL!!! 🚨", bg="#ffcccc", fg="red", font=("Arial", 14, "bold"))
    else:
        result_label.config(text="✅ It's a Safe Email!", bg="#ccffcc", fg="green", font=("Arial", 14, "bold"))

# Function to toggle dark/light mode
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.configure(bg="#1E1E1E")  # Dark mode background
        title_label.config(bg="#1E1E1E", fg="white")
        input_text.config(bg="#2E2E2E", fg="white", insertbackground="white")
        check_button.config(bg="#4A90E2", fg="white")
        result_label.config(bg="#333333", fg="white")
        toggle_button.config(bg="#4A90E2", fg="white", text="🌙", relief="flat")
    else:
        root.configure(bg="#D0EFFF")  # Light blue theme background
        title_label.config(bg="#D0EFFF", fg="#004466")
        input_text.config(bg="white", fg="black", insertbackground="black")
        check_button.config(bg="#0084FF", fg="white")
        result_label.config(bg="white", fg="black")
        toggle_button.config(bg="#0084FF", fg="white", text="☀", relief="flat")

# Create main window with a light blue theme
root = ThemedTk(theme="adapta")
root.title("Spam Hunter")
root.geometry("450x420")
root.configure(bg="#D0EFFF")  # Default light blue background

# Initial mode (Light mode enabled by default)
dark_mode = False

# Title Label
title_label = tk.Label(root, text="Spam Hunter", font=("Arial", 18, "bold"), fg="#004466", bg="#D0EFFF")
title_label.pack(pady=10)

# Toggle button for theme switch
toggle_button = tk.Button(root, text="☀", font=("Arial", 12, "bold"), bg="#0084FF", fg="white",
                          width=3, height=1, command=toggle_theme, relief="flat", borderwidth=0)
toggle_button.pack(anchor="ne", padx=10, pady=5)

# Text Input (Scrolled Text)
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=4, font=("Arial", 11),
                                       bg="white", fg="black", insertbackground="black", borderwidth=2, relief="solid")
input_text.pack(pady=10)

# Spam Check Button (Aesthetic Rounded Button)
style = Style(theme="darkly")
check_button = tk.Button(root, text="🚀 Check Spam", font=("Arial", 13, "bold"), bg="#0084FF", fg="white",
                         width=15, height=1, command=predict_spam, borderwidth=0, relief="flat")
check_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 13, "bold"), width=40, height=3, bg="white", fg="black",
                        borderwidth=2, relief="solid")
result_label.pack(pady=10)

# Run the app
root.mainloop()
