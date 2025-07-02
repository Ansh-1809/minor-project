import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import matplotlib.pyplot as plt

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Expense Tracker")

        self.expenses = []

       
        self.description_label = tk.Label(root, text="Expense Description:")
        self.description_label.pack(pady=5)

        self.description_entry = tk.Entry(root)
        self.description_entry.pack(pady=5)

        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.pack(pady=5)

        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack(pady=5)

        self.add_expense_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_expense_button.pack(pady=5)

        self.view_expenses_button = tk.Button(root, text="View Expenses", command=self.view_expenses)
        self.view_expenses_button.pack(pady=5)

        self.save_expenses_button = tk.Button(root, text="Save Expenses", command=self.save_expenses)
        self.save_expenses_button.pack(pady=5)

        self.load_expenses_button = tk.Button(root, text="Load Expenses", command=self.load_expenses)
        self.load_expenses_button.pack(pady=5)

        self.visualize_expenses_button = tk.Button(root, text="Visualize Expenses", command=self.visualize_expenses)
        self.visualize_expenses_button.pack(pady=5)

        
        self.total_label = tk.Label(root, text="")
        self.total_label.pack(pady=10)

        
        self.load_expenses()
        self.update_total()

    def add_expense(self):
        description = self.description_entry.get()
        amount = self.amount_entry.get()

        if description and amount:
            try:
                amount = float(amount)
                self.expenses.append((description, amount))
                self.update_total()
                self.description_entry.delete(0, tk.END)
                self.amount_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid amount.")
        else:
            messagebox.showwarning("Input Error", "Please fill in both fields.")

    def view_expenses(self):
        if self.expenses:
            expenses_str = "\n".join([f"{desc}: ${amt:.2f}" for desc, amt in self.expenses])
            messagebox.showinfo("Expenses", expenses_str)
        else:
            messagebox.showinfo("Expenses", "No expenses recorded.")

    def save_expenses(self):
        with open("expenses.txt", "w") as file:
            for desc, amt in self.expenses:
                file.write(f"{desc},{amt}\n")
        messagebox.showinfo("Save Expenses", "Expenses saved successfully.")

    def load_expenses(self):
        if os.path.exists("expenses.txt"):
            with open("expenses.txt", "r") as file:
                self.expenses = [line.strip().split(",") for line in file.readlines()]
                self.expenses = [(desc, float(amt)) for desc, amt in self.expenses]
        self.update_total()

    def update_total(self):
        total = sum(amt for _, amt in self.expenses)
        self.total_label.config(text=f"Total Expenses: ${total:.2f}")

    def visualize_expenses(self):
        if self.expenses:
            descriptions = [desc for desc, _ in self.expenses]
            amounts = [amt for _, amt in self.expenses]

            plt.bar(descriptions, amounts)
            plt.xlabel('Description')
            plt.ylabel('Amount ($)')
            plt.title('Expenses Visualization')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            messagebox.showinfo("Visualization", "No expenses recorded to visualize.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()