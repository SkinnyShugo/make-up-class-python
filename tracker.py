import json

# Initialize variables
income = 0.0
expenses = []
savings = 0.0

# Load transaction data from file
def load_data():
    global income, expenses, savings
    try:
        with open("transactions.json", "r") as file:
            data = json.load(file)
            income = data.get("income", 0.0)
            expenses = data.get("expenses", [])
            savings = data.get("savings", 0.0)
    except FileNotFoundError:
        pass

# Save transaction data to file
def save_data():
    data = {
        "income": income,
        "expenses": expenses,
        "savings": savings
    }
    with open("transactions.json", "w") as file:
        json.dump(data, file)

# Add income
def add_income():
    global income
    amount = float(input("Enter income amount: "))
    income += amount
    print(f"Income of {amount} added successfully.")

# Add expense
def add_expense():
    global expenses
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    expense = {
        "description": description,
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    print("Expense added successfully.")

# Calculate savings
def calculate_savings():
    global savings
    savings = income - sum(expense["amount"] for expense in expenses)
    print(f"Total savings: {savings}")

# Generate expense report by category
def generate_expense_report_by_category():
    category = input("Enter category for expense report: ")
    total_amount = sum(expense["amount"] for expense in expenses if expense["category"] == category)
    print(f"Total expenses for {category}: {total_amount}")

# Main program loop
def main():
    load_data()

    while True:
        print("===== Personal Finance Tracker =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Savings")
        print("4. Generate Expense Report by Category")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            calculate_savings()
        elif choice == "4":
            generate_expense_report_by_category()
        elif choice == "5":
            save_data()
            print("Thank you for using the Personal Finance Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
