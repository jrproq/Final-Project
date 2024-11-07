import tkinter as tk
import sqlite3
from tkinter import messagebox

class DatabaseApp:
    def init(self, root):
        self.root = root
        self.root.title("Inventory Management System")

        # Create a database or connect to an existing one
        self.conn = sqlite3.connect("inventory.db")
        self.cursor = self.conn.cursor()

        # Create a table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)''')
        self.conn.commit()

        # Create GUI elements
        self.task_label = tk.Label(root, text="Task:")
        self.task_label.pack()

        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root)
        self.task_listbox.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
            self.conn.commit()
            self.load_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please input a task.")

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)