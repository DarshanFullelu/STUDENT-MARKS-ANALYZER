import tkinter as tk
from tkinter import messagebox

def get_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F (fail)'

def analyze():
    try:
    
        marks = [
            float(entry1.get()),
            float(entry2.get()),
            float(entry3.get()),
            float(entry4.get()),
            float(entry5.get())
        ]
        
        total = sum(marks)
        average = total / 5
        grade = get_grade(average)

        result_label.config(
            text=f"Total: {total} | Average: {average:.2f} | Grade: {grade}",
            fg="blue"
        )
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for all marks.")

root = tk.Tk()
root.title("Student Marks Analyzer")
root.geometry("350x400")
root.resizable(False, False)

tk.Label(root, text="Enter Marks for 5 Subjects:", font=("Arial", 14)).pack(pady=10)

entry1 = tk.Entry(root, font=("Arial", 12))
entry1.pack(pady=5)
entry1.insert(0, "Subject 1")

entry2 = tk.Entry(root, font=("Arial", 12))
entry2.pack(pady=5)
entry2.insert(0, "Subject 2")

entry3 = tk.Entry(root, font=("Arial", 12))
entry3.pack(pady=5)
entry3.insert(0, "Subject 3")

entry4 = tk.Entry(root, font=("Arial", 12))
entry4.pack(pady=5)
entry4.insert(0, "Subject 4")

entry5 = tk.Entry(root, font=("Arial", 12))
entry5.pack(pady=5)
entry5.insert(0, "Subject 5")

tk.Button(root, text="Analyze Marks", command=analyze, font=("Arial", 12), bg="green", fg="white").pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 13))
result_label.pack(pady=10)

root.mainloop()