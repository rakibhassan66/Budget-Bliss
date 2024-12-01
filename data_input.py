# data_input.py

def get_initial_budget():
    while True:
        try:
            budget = float(input("Enter your initial budget (Taka): "))
            if budget <= 0:
                raise ValueError("Budget must be a positive number.")
            return budget
        except ValueError as e:
            print(e)

def get_expense_input():
    expense = float(input("Enter your expense amount: "))
    category = input("Enter the category of the expense (e.g., food, rent): ")
    description = input("Enter a description for the expense: ")
    return expense, category, description
