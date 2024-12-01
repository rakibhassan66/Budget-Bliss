# visualization.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_expenses(finances):
    """Plot a bar chart of expenses by category."""
    categories = [expense['category'] for expense in finances['expenses']]
    expenses = [expense['expense'] for expense in finances['expenses']]
    
    expense_data = pd.DataFrame({'Category': categories, 'Expense': expenses})
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Category', y='Expense', data=expense_data)
    plt.title('Expenses by Category')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_balance(finances):
    """Plot the current balance vs. total spent."""
    labels = ['Current Balance', 'Total Spent']
    values = [finances['current_balance'], finances['total_spent']]
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Current Balance vs Total Spent')
    plt.show()
