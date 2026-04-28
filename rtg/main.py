import tkinter as tk
from tkinter import messagebox, ttk
import random
import json
import os
class RandomTaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Task Generator")
        self.root.geometry("400x500")
        self.predefined_tasks = [
            {"text": "Прочитать статью", "category": "учёба"},
            {"text": "Сделать зарядку", "category": "спорт"},
            {"text": "Разобрать почту", "category": "работа"},
            {"text": "Выучить 5 слов", "category": "учёба"},
            {"text": "Пробежка 15 мин", "category": "спорт"}
        ]
        self.history = []
        self.load_history()
        self.setup_ui()
        self.update_history_display()
    def setup_ui(self):
        tk.Button(self.root, text="Сгенерировать задачу", command=self.generate_task, bg="#4CAF50", fg="white").pack(pady=10)
        filter_frame = tk.Frame(self.root)
        filter_frame.pack(pady=5)
        tk.Label(filter_frame, text="Фильтр:").pack(side=tk.LEFT)
        self.filter_var = tk.StringVar(value="Все")
        filter_menu = ttk.Combobox(filter_frame, textvariable=self.filter_var, values=["Все", "учёба", "спорт", "работа"])
        filter_menu.pack(side=tk.LEFT, padx=5)
        filter_menu.bind("<<ComboboxSelected>>", lambda e: self.update_history_display())
        tk.Label(self.root, text="История задач:").pack()
        self.history_listbox = tk.Listbox(self.root, width=50, height=15)
        self.history_listbox.pack(pady=5, padx=10)
    def generate_task(self):
        task = random.choice(self.predefined_tasks)
        self.history.append(task)
        self.save_history()
        self.update_history_display()
        messagebox.showinfo("Новая задача", f"{task['text']} ({task['category']})")
    def update_history_display(self):
        self.history_listbox.delete(0, tk.END)
        category_filter = self.filter_var.get()
        for task in reversed(self.history):
            if category_filter == "Все" or task['category'] == category_filter:
                self.history_listbox.insert(tk.END, f"[{task['category']}] {task['text']}")
    def save_history(self):
        with open("history.json", "w", encoding="utf-8") as f:
            json.dump(self.history, f, ensure_ascii=False, indent=4)
    def load_history(self):
        if os.path.exists("history.json"):
            with open("history.json", "r", encoding="utf-8") as f:
                self.history = json.load(f)
if __name__ == "__main__":
    root = tk.Tk()
    app = RandomTaskApp(root)
    root.mainloop()
