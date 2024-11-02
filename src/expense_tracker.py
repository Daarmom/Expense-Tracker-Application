# src/expense_tracker.py
import csv
from expense import Expense
from category import Category

class ExpenseTracker:
    def __init__(self, data_file="data/expenses.csv"):
        self.expenses = []
        self.categories = []
        self.data_file = data_file
        self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.data_file, mode="r") as file:
                reader = csv.reader(file)
                for row in reader:
                    amount, date, category, description = row
                    self.expenses.append(Expense(float(amount), date, category, description))
        except FileNotFoundError:
            pass  # File will be created when an expense is added

    def save_expenses(self):
        with open(self.data_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            for expense in self.expenses:
                writer.writerow([expense.amount, expense.date, expense.category, expense.description])

    def add_expense(self, amount, date, category, description=""):
        new_expense = Expense(amount, date, category, description)
        self.expenses.append(new_expense)
        self.save_expenses()

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)
            self.save_expenses()

    def view_expenses(self):
        for expense in self.expenses:
            print(expense)
