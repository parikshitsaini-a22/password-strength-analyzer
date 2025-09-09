import tkinter as tk
from tkinter import filedialog, messagebox
from .analyzer import analyze_password
from .wordlist import generate_wordlist

def run_gui():
    root = tk.Tk()
    root.title("Password Strength Analyzer")
    root.configure(bg="black")

    label = tk.Label(root, text="Enter Password:", fg="red", bg="black")
    label.pack(pady=5)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    def analyze():
        pw = password_entry.get()
        score, feedback = analyze_password(pw)
        messagebox.showinfo("Analysis", f"Score: {score}/4\nFeedback: {feedback}")

    analyze_btn = tk.Button(root, text="Analyze", command=analyze, bg="red", fg="white")
    analyze_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
