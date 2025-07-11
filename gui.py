import tkinter as tk
from tkinter import messagebox
from analyzer import analyze_password
from generator import collect_inputs, generate_variations, save_wordlist

def run_analysis():
    pwd = password_entry.get()
    if not pwd:
        messagebox.showerror("Error", "Please enter a password.")
        return

    result = analyze_password(pwd)
    feedback = "\n".join(result['feedback']['suggestions']) or "Good password!"
    output = (
        f"Score: {result['score']} / 4\n"
        f"Crack Time: {result['crack_time']}\n"
        f"Feedback: {feedback}"
    )
    result_label.config(text=output)

def generate_wordlist():
    name = name_entry.get()
    dob = dob_entry.get()
    pet = pet_entry.get()

    if not (name or dob or pet):
        messagebox.showerror("Error", "Enter at least one field: name, dob, or pet.")
        return

    base_words = collect_inputs(name, dob, pet)
    wordlist = generate_variations(base_words)
    save_wordlist(wordlist)
    messagebox.showinfo("Success", f"Wordlist saved with {len(wordlist)} entries.")

# GUI Setup
root = tk.Tk()
root.title("🔐 Password Strength Analyzer + Wordlist Generator")
root.geometry("450x400")

tk.Label(root, text="Enter Password:").pack()
password_entry = tk.Entry(root, show="*", width=40)
password_entry.pack()

tk.Label(root, text="Enter Name:").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Enter DOB (YYYY-MM-DD):").pack()
dob_entry = tk.Entry(root, width=40)
dob_entry.pack()

tk.Label(root, text="Enter Pet Name:").pack()
pet_entry = tk.Entry(root, width=40)
pet_entry.pack()

tk.Button(root, text="🔍 Analyze Password", command=run_analysis).pack(pady=10)
tk.Button(root, text="🛠 Generate Wordlist", command=generate_wordlist).pack(pady=5)

result_label = tk.Label(root, text="", fg="blue", justify="left")
result_label.pack(pady=10)

root.mainloop()
