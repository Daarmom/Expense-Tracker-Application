# Expense-Tracker-Application

This is a Python-based expense tracker application designed to help users track their daily expenses.
The app uses Object-Oriented Programming principles and CSV files for data storage.

Setup Instructions
Prerequisites
Python 3.x is required to run this application. You can download it from python.org.
A code editor (such as VS Code) or terminal for running Python scripts.

Steps to Setup Locally:

Clone the Repository
» git clone <repository_url>
» cd expense-tracker

Install Required Packages If any dependencies are used, install them using requirements.txt:
» pip install -r requirements.txt

Run the Application
» python src/main.py

Setup CSV File (Optional)

The application automatically creates data/expenses.csv if it does not exist.
Ensure that data/ directory exists in the root project folder.

1. Project Setup and Initial Development

● Set up the project repository on GitHub for version control.
● Created the project structure, including separate directories for src/ (source code) and
data/ (CSV files).
● Implemented the core classes: Expense, Category, and ExpenseTracker using
object-oriented principles.
● Built the main functions for adding, deleting, and viewing expenses.

Key Deliverables:
● GitHub repository with project structure.
● Core Python classes implemented.
● Basic functionality for adding and viewing expenses.

2. Category Management System

● Implemented functionality to categorize expenses by user-defined categories such as
groceries, utilities, and entertainment.
● Allow filtering of expenses by category to provide insights into specific spending areas.

Key Deliverables:
● Ability to assign categories to expenses.
● A filtering system to display expenses for specific categories.

3. Report Generation and File Handling

● Created functionality to generate reports showing total expenses for specific periods
(daily, weekly, monthly).
● Implemented file handling for saving expenses to a CSV file and loading them upon
starting the application.
● Ensure that the CSV file persists between sessions.

Key Deliverables:
● Report generation based on time periods.
● CSV file handling for saving and loading expense data.

4. Error Handling and User Input Validation

● Implemented robust error handling for user input errors (e.g., invalid dates, negative
amounts) and file operation errors (e.g., file not found).
● Ensure that invalid inputs do not crash the application and that users receive appropriate
error messages.

Key Deliverables:
● Error handling for common input and file operation issues.
● Graceful handling of invalid user inputs.

5. Version Control and Documentation

● Use Git for tracking changes throughout the development process, ensuring commits are
well-documented.
