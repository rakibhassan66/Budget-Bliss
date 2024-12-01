# main.py
import data_input
import expense_tracker
import dashboard

def main():
    print("Welcome to Personal Finance Tracker!")
    
    # Get the initial budget from the user
    budget = data_input.get_initial_budget()
    
    # Initialize finances
    finances = expense_tracker.initialize_finances(budget)

    while True:
        print("\nOptions: ")
        print("1. Add Expense")
        print("2. Add Loan")
        print("3. View Dashboard")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            expense, category, description = data_input.get_expense_input()
            expense_tracker.add_expense(finances, expense, category, description)
        
        elif choice == "2":
            lender_name = input("Enter lender name: ")
            amount = float(input("Enter loan amount: "))
            return_date = input("Enter loan return date (YYYY-MM-DD): ")
            expense_tracker.add_loan(finances, lender_name, amount, return_date)
        
        elif choice == "3":
            dashboard.display_dashboard(finances)
        
        elif choice == "4":
            print("Exiting... Have a good day!")
            expense_tracker.save_finances_to_csv(finances)
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
