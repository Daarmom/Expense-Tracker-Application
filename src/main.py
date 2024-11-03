# src/main.py

from expense_tracker import ExpenseTracker
from category import Category
import datetime

def display_menu():
    print("\nExpense Tracker")
    print("1. View all expenses")
    print("2. Add an expense")
    print("3. Delete an expense")
    print("4. View all categories")
    print("5. Add a category")
    print("6. Filter expenses by category")
    print("7. Generate Report")
    print("8. Exit")
    print("\nChoose an option:")

def add_expense(expense_tracker):
    try:
        amount = float(input("Enter amount: "))
        date_input = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
        date = date_input if date_input else datetime.date.today().isoformat()
        
        expense_tracker.view_categories()
        category = input("Enter category name: ")
        description = input("Enter description (optional): ")

        # Add the expense to the tracker
        expense_tracker.add_expense(amount, date, category, description)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input!")

def add_category(expense_tracker):
    name = input("Enter category name: ")
    expense_tracker.add_category(name)

def filter_expenses(expense_tracker):
    category_name = input("Enter the category name to filter by: ")
    expense_tracker.filter_expenses_by_category(category_name)

def delete_expense(expense_tracker):
    try:
        expense_tracker.view_expenses()
        index = int(input("Enter the index of the expense to delete: "))
        
        # Delete the expense by index
        expense_tracker.delete_expense(index)
        print("Expense deleted successfully!")
    except (ValueError, IndexError):
        print("Invalid index! Please enter a valid number.")

def generate_report(expense_tracker):
    period = input("Enter the period for the report (daily, weekly, monthly): ").lower()
    expense_tracker.generate_report(period)

def main():
    expense_tracker = ExpenseTracker()

    while True:
        display_menu()
        choice = input("Select an option (1-8): ")

        if choice == '1':
            # View all expenses
            print("\nAll Expenses:")
            expense_tracker.view_expenses()
        elif choice == '2':
            # Add a new expense
            add_expense(expense_tracker)
        elif choice == '3':
            # Delete an expense
            delete_expense(expense_tracker)
        elif choice == '4':
            # View all categories
            print("\nCategories:")
            expense_tracker.view_categories()
        elif choice == '5':
            # Add a new category
            add_category(expense_tracker)
        elif choice == '6':
            # Filter expenses by category
            filter_expenses(expense_tracker)
        elif choice == '7':
            # Filter expenses by category
            generate_report(expense_tracker)
        elif choice == '8':
            # Exit the application
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
