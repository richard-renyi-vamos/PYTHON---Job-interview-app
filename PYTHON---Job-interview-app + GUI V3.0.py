import tkinter as tk
import random

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

categories = {
    "Behavioral": [questions[3], questions[4], questions[7]],
    "Personal": [questions[0], questions[5]],
    "Professional": [questions[1], questions[2], questions[6]],
}

tips = [
    "Research the company and role before the interview.",
    "Practice answering common interview questions out loud.",
    "Dress appropriately and be on time.",
    "Show confidence but stay humble.",
    "Prepare questions to ask the interviewer.",
    "Use the STAR method for answering behavioral questions.",
]

favorites = []
question_count = 0
dark_mode = False

def get_random_question():
    global question_count
    question_label.config(text=random.choice(questions))
    question_count += 1
    counter_label.config(text=f"Questions practiced: {question_count}")

def get_random_tip():
    tip_label.config(text=random.choice(tips))

def save_answer():
    ans = answer_entry.get("1.0", tk.END).strip()
    if ans:
        with open("answers.txt", "a") as f:
            f.write(f"{question_label.cget('text')}\nAnswer: {ans}\n\n")
        answer_entry.delete("1.0", tk.END)

def add_to_favorites():
    q = question_label.cget("text")
    if q and q not in favorites:
        favorites.append(q)

def show_favorites():
    fav_win = tk.Toplevel(root)
    fav_win.title("Favorites")
    for fav in favorites:
        tk.Label(fav_win, text=fav, wraplength=350).pack(anchor="w", padx=10)

def get_question_by_category(cat):
    question_label.config(text=random.choice(categories[cat]))

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    bg = "#2E2E2E" if dark_mode else "SystemButtonFace"
    fg = "white" if dark_mode else "black"
    root.configure(bg=bg)
    for widget in root.winfo_children():
        try:
            widget.configure(bg=bg, fg=fg)
        except:
            pass

def open_settings():
    win = tk.Toplevel(root)
    win.title("Settings")
    tk.Label(win, text="Settings", font=("Arial", 14)).pack(pady=10)
    tk.Button(win, text="Toggle Dark Mode", command=toggle_dark_mode).pack(pady=10)

root = tk.Tk()
root.title("Job Interview Prep")
root.geometry("520x520")

frame = tk.Frame(root)
frame.pack(pady=10)

question_label = tk.Label(frame, text="Click below to get a question", wraplength=400, font=("Arial", 12))
question_label.pack()

tk.Button(frame, text="Get a Question", command=get_random_question).pack(pady=5)
tk.Button(root, text="Behavioral", command=lambda: get_question_by_category("Behavioral")).pack(side="left", padx=5)
tk.Button(root, text="Personal", command=lambda: get_question_by_category("Personal")).pack(side="left", padx=5)
tk.Button(root, text="Professional", command=lambda: get_question_by_category("Professional")).pack(side="left", padx=5)

tip_label = tk.Label(frame, text="Click below for a tip", wraplength=400, fg="blue", font=("Arial", 12))
tip_label.pack()
tk.Button(frame, text="Get a Tip", command=get_random_tip).pack(pady=5)

answer_entry = tk.Text(frame, height=4, width=50)
answer_entry.pack()
tk.Button(frame, text="Save Answer", command=save_answer).pack(pady=5)

tk.Button(root, text="Add to Favorites", command=add_to_favorites).pack()
tk.Button(root, text="Show Favorites", command=show_favorites).pack()
tk.Button(root, text="Settings", command=open_settings).pack(pady=10)

counter_label = tk.Label(root, text="Questions practiced: 0", font=("Arial", 10))
counter_label.pack(pady=5)

root.mainloop()
