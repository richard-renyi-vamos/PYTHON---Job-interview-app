import tkinter as tk
import random

# Question bank
questions = [
    "Tell me about yourself.",
    "What are your strengths and weaknesses?",
    "Why do you want to work here?",
    "Describe a challenging project you've worked on.",
    "How do you handle conflict in a team?",
    "Where do you see yourself in five years?",
    "Why should we hire you?",
    "Tell me about a time you failed and how you handled it.",
]

tips = [
    "Research the company and role before the interview.",
    "Practice answering common interview questions out loud.",
    "Dress appropriately and be on time.",
    "Show confidence but stay humble.",
    "Prepare questions to ask the interviewer.",
    "Use the STAR method for answering behavioral questions.",
]

def get_random_question():
    question_label.config(text=random.choice(questions))

def get_random_tip():
    tip_label.config(text=random.choice(tips))

def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")
    settings_window.geometry("300x200")
    tk.Label(settings_window, text="Settings", font=("Arial", 14)).pack(pady=10)
    tk.Label(settings_window, text="No settings available yet.").pack(pady=10)

# GUI setup
root = tk.Tk()
root.title("Job Interview Preparation")
root.geometry("500x300")

frame = tk.Frame(root)
frame.pack(pady=20)

question_label = tk.Label(frame, text="Click below to get a question", wraplength=400, font=("Arial", 12))
question_label.pack()

question_button = tk.Button(frame, text="Get a Question", command=get_random_question)
question_button.pack(pady=10)

tip_label = tk.Label(frame, text="Click below for a tip", wraplength=400, font=("Arial", 12), fg="blue")
tip_label.pack()

tip_button = tk.Button(frame, text="Get a Tip", command=get_random_tip)
tip_button.pack(pady=10)

settings_button = tk.Button(root, text="Settings", command=open_settings)
settings_button.pack(pady=10)

root.mainloop()
