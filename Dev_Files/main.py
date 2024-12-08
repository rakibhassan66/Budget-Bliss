from data_input import DataInput
from expense_tracker import Finances
from dashboard import Dashboard

def main():
    print("Welcome to Personal Finance Tracker!")

    # Initialize input and dashboard objects
    data_input = DataInput()
    budget = data_input.get_initial_budget()
    finances = Finances(budget)
    dashboard = Dashboard()

    while True:
        print("\nOptions: ")
        print("1. Add Expense")
        print("2. Add Loan")
        print("3. View Dashboard")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            expense, category, description = data_input.get_expense_input()
            finances.add_expense(expense, category, description)

        elif choice == "2":
            lender_name = input("Enter lender name: ")
            amount = float(input("Enter loan amount: "))
            return_date = input("Enter loan return date (YYYY-MM-DD): ")
            finances.add_loan(lender_name, amount, return_date)

        elif choice == "3":
            dashboard.display_dashboard(finances)
            dashboard.display_graph(finances)

        elif choice == "4":
            print("Exiting... Have a good day!")
            finances.save_to_csv()
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
