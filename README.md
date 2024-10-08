# Expense Tracker

This project is a comprehensive expense tracker that allows users to manage their finances effectively. It includes multiple apps for handling different aspects of personal finance, including income, expenses, budgets, recurring transactions, and reporting.

## Features

- **User Management (`user_app`)**:
  - Users can create accounts and authenticate using tokens generated with Django REST Framework's `authtoken`.
  - Tokens are generated when users register or log in, providing authorization to access other apps.
  - Tokens are destroyed when users log out, ensuring secure access control.

- **Income Management (`income_app`)**:
  - Users can log and manage their income sources.
  - Supports recurring income entries, such as monthly salary or dividends.

- **Expense Management (`expense_app`)**:
  - Users can record and categorize their expenses.
  - Supports both one-time and recurring expenses, such as bills and subscriptions.

- **Budget Management (`budget_app`)**:
  - Users can create and manage budgets to track spending.
  - Allows users to compare actual expenses against the set budget.

- **Recurring Transactions (`recurring_app`)**:
  - Manages recurring income and expenses automatically.
  - Integrates with both the `income_app` and `expense_app` to handle recurring financial activities.

- **Reporting (`report_app`)**:
  - Generates detailed reports summarizing income, expenses, and budgets.
  - Provides insights into financial health, including net savings and expense categories.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TeraByte07/expense_tracker.git
   cd your-repository-name

2.  **Set up the virtual environment**:

bash
Copy code
python -m venv env
env\Scripts\activate  # For Windows
# source env/bin/activate  # For macOS/Linux


3:  **Install dependencies**:

bash
Copy code
pip install -r requirements.txt

4:  **Apply migrations**:

bash
Copy code
python manage.py migrate

5:  **Create a superuser (optional, for admin access)**:

bash
Copy code
python manage.py createsuperuser

6:  **Run the development server**:

bash
Copy code
python manage.py runserver

**Usage**
**User Registration and Authentication**:

Users can sign up and receive an authentication token.
The token must be included in the Authorization header for accessing the income, expense, budget, recurring, and report functionalities.
Managing Income:

**Add, view, update, and delete income entries.**
Set up recurring income to automatically log earnings.
Managing Expenses:

**Add, view, update, and delete expenses.**
Categorize expenses and set up recurring entries for regular bills.
Budgeting:

**Create and manage budgets.**
Track spending and compare it to the budgeted amounts.
Generating Reports:

**Generate reports summarizing financial activities.**
Analyze net savings, categorize expenses, and track financial health.

**Contributing**
Contributions are welcome! Please fork the repository and submit a pull request with your changes.# expenseTracker
