import matplotlib.pyplot as plt

class Dashboard:
    """Handles dashboard display and visualization."""

    @staticmethod
    def display_dashboard(finances):
        """Display the financial dashboard."""
        days_remaining = 31 - len(set([exp['date'][:10] for exp in finances.expenses]))
        daily_limit = finances.calculate_daily_limit(days_remaining)

        print("\n===== Financial Dashboard =====")
        print(f"Budget: {finances.budget} Taka")
        print(f"Total Spent: {finances.total_spent} Taka")
        print(f"Total Deposits: {finances.total_deposits} Taka")
        print(f"Current Balance: {finances.current_balance} Taka")
        print(f"Remaining Days: {days_remaining}")
        print(f"Daily Spending Limit: {daily_limit:.2f} Taka")
        print(f"Rate of Waste: {finances.total_spent / finances.budget * 100:.2f}%")

    @staticmethod
    def display_graph(finances):
        """Display graphs for current balance and spending."""
        # Bar chart for Current Balance and Total Spent
        labels = ['Current Balance', 'Total Spent']
        values = [finances.current_balance, finances.total_spent]

        plt.bar(labels, values, color=['green', 'red'])
        plt.title("Financial Overview")
        plt.ylabel("Amount (Taka)")
        plt.tight_layout()
        plt.show()
