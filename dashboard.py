# dashboard.py
from visualization import plot_expenses, plot_balance

def display_dashboard(finances):
    """Display the financial dashboard."""
    print("\n===== Financial Dashboard =====")
    print(f"Budget: {finances['budget']} Taka")
    print(f"Total Spent: {finances['total_spent']} Taka")
    print(f"Total Deposits: {finances['total_deposits']} Taka")
    print(f"Current Balance: {finances['current_balance']} Taka")
    print(f"Daily Spending Limit: {finances['daily_limit']} Taka")
    print(f"Rate of Waste: {finances['total_spent'] / finances['budget'] * 100:.2f}%")

    # Display visualizations
    plot_expenses(finances)
    plot_balance(finances)
