# expense_tracker.py
import pandas as pd
from datetime import datetime

def initialize_finances(budget):
    """Create an initial record for tracking finances."""
    return {
        'budget': budget,
        'expenses': [],
        'loans': [],
        'total_spent': 0,
        'total_deposits': 0,
        'current_balance': budget,
        'daily_limit': budget / 30
    }

def add_expense(finances, expense, category, description):
    """Add an expense and update the total."""
    finances['expenses'].append({
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'expense': expense,
        'category': category,
        'description': description
    })
    finances['total_spent'] += expense
    finances['current_balance'] -= expense

def add_loan(finances, lender_name, amount, return_date):
    """Record a loan taken."""
    finances['loans'].append({
        'lender': lender_name,
        'amount': amount,
        'date_taken': datetime.now().strftime("%Y-%m-%d"),
        'return_date': return_date
    })
    finances['total_deposits'] += amount
    finances['current_balance'] += amount

def save_finances_to_csv(finances, file_path="assets/finances.csv"):
    """Save current financial data to CSV."""
    df = pd.DataFrame(finances['expenses'])
    df.to_csv(file_path, index=False)
