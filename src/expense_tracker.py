# src/expense_tracker.py
import csv
import os
from expense import Expense
from category import Category
from datetime import datetime, timedelta

class ExpenseTracker:
    def __init__(self, data_file="data/expenses.csv"):
        self.expenses = []
        self.categories = []
        self.data_file = data_file
        self.load_expenses()
        self.category_id_counter = 1  # To give each new category a unique ID

    def load_expenses(self):
        if not os.path.exists(self.data_file):
            print(f"File '{self.data_file}' not found. Starting with an empty expense list.")
            return
        try:
            with open(self.data_file, mode="r") as file:
                reader = csv.reader(file)
                for row in reader:
                    amount, date, category, description = row
                    self.expenses.append(Expense(float(amount), date, category, description))
            print("Expenses loaded successfully!")
        except Exception as e:
            print(f"Error loading expenses: {e}")

    def save_expenses(self):
        try:
            with open(self.data_file, mode="w", newline="") as file:
                writer = csv.writer(file)
                for expense in self.expenses:
                    writer.writerow([expense.amount, expense.date, expense.category, expense.description])
                print("Expenses saved successfully!")
        except Exception as e:
            print(f"Error saving expenses: {e}")

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

    # Category Management Methods
    def add_category(self, name):
        new_category = Category(self.category_id_counter, name)
        self.categories.append(new_category)
        self.category_id_counter += 1
        print(f"Category '{name}' added with ID {new_category.id}")

    def view_categories(self):
        for category in self.categories:
            print(category)

    def filter_expenses_by_category(self, category_name):
        filtered_expenses = [expense for expense in self.expenses if expense.category == category_name]
        if filtered_expenses:
            print(f"\nExpenses for category '{category_name}':")
            for expense in filtered_expenses:
                print(expense)
        else:
            print(f"No expenses found for category '{category_name}'")

    # Report Generation - Calculate total expenses for a given period
    def generate_report(self, period):
        if period == 'daily':
            report_date = datetime.today().date()
        elif period == 'weekly':
            report_date = datetime.today().date() - timedelta(days=7)
        elif period == 'monthly':
            report_date = datetime.today().replace(day=1).date()
        else:
            print("Invalid period! Choose from 'daily', 'weekly', or 'monthly'.")
            return

        # Filter and sum expenses within the specified period
        total = 0
        print(f"\nExpenses for the {period} report:")
        for expense in self.expenses:
            expense_date = datetime.strptime(expense.date, "%Y-%m-%d").date()
            if period == 'daily' and expense_date == report_date:
                print(expense)
                total += expense.amount
            elif period == 'weekly' and expense_date >= report_date:
                print(expense)
                total += expense.amount
            elif period == 'monthly' and expense_date >= report_date:
                print(expense)
                total += expense.amount

        print(f"\nTotal {period} expenses: ${total:.2f}")
