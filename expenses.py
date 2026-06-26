import json
import sys
from datetime import datetime

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d")

def load_expenses():
    with open("expenses.json", "r") as file:
        return json.load(file)

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

if len(sys.argv) < 2:
    print("Please provide a command: add, list, delete, update, summary")
    sys.exit(1)
command = sys.argv[1]
if command == "add":
    if len(sys.argv) < 4:
        print("Please provide a description and amount for the expense.")
        sys.exit(1)
    if len (sys.argv) > 4:
        print("Please provide only a description and amount for the expense.")
        sys.exit(1)
    expenses = load_expenses()
    highest_id = max(expense["id"] for expense in expenses) if expenses else 0
    try:
        description = (sys.argv[2])
        amount = float(sys.argv[3])
    except ValueError:
        print("Please provide a valid description and amount for the expense.")
        sys.exit(1)
    new_expense = {
        "id": highest_id + 1,
        "description": description,
        "amount": amount,
        "date": timestamp
    }
    expenses.append(new_expense)
    print("Expense added to memory!")
    save_expenses(expenses)

elif command == "list":
    expenses = load_expenses()
    if len(sys.argv) == 2:
        print(
            f"{'ID':<5}"
            f"{'Date':<12}"
            f"{'Description':<18}"
            f"{'Amount':<10}"
        )
        for expense in expenses:
            print(
                f"{expense['id']:<5}"
                f"{expense['date'].split(' ')[0]:<12}"
                f"{expense['description']:<18}"
                f"${expense['amount']:.2f}"
                )
    else:
        print("Please provide only the 'list' command to see all expenses.")
        sys.exit(1)

elif command == "delete":
    if len(sys.argv) < 3:
        print("Please provide an expense ID to delete. Use 'list' to see available IDs.")
        sys.exit(1)
    if len (sys.argv) > 3:
        print("Please provide only an expense ID to delete. Use 'list' to see available IDs.")
        sys.exit(1)
    expenses = load_expenses()
    try:
        expense_id = int(sys.argv[2])
    except ValueError:
        print("Please provide a valid expense ID to delete. Use 'list' to see available IDs.")
        sys.exit(1)
    found = False
    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            found = True
            break
    if not found:
        print(f"Expense ID not found!")
        sys.exit(1)
    print(f"Expense with ID: {expense_id} deleted!")
    save_expenses(expenses)

elif command == "update":
    if len(sys.argv) < 5:
        print("Please provide an expense ID, description, and amount to update. Use 'list' to see available IDs.")
        sys.exit(1)
    if len (sys.argv) > 5:
        print("Please provide only an expense ID, description, and amount to update. Use 'list' to see available IDs.")
        sys.exit(1)
    expenses = load_expenses()
    try:
        expense_id = int(sys.argv[2])
    except ValueError:
        print("Please provide a valid expense ID to update. Use 'list' to see available IDs.")
        sys.exit(1)
    found = False
    for expense in expenses:
        if expense["id"] == expense_id:
            try:
                expense["description"] = (sys.argv[3])
                expense["amount"] = float(sys.argv[4])
                found = True
                break
            except ValueError:
                print("Please provide valid values for the expense description and amount.")
                sys.exit(1)
    if not found:
        print(f"Expense ID not found!")
        sys.exit(1)
    print(f"Expense with ID: {expense_id} updated!")
    save_expenses(expenses)

elif command == "summary":
    expenses = load_expenses()
    total_amount = sum(expense["amount"] for expense in expenses)
    if len(sys.argv) == 2:
        print(f"Total expenses: ${total_amount:.2f}")
        print(f"Don't forget to save and invest!")
    elif sys.argv[2] == "month":
        if len(sys.argv) < 4:
            print("Please provide a month (1-12) for the summary.")
            sys.exit(1)
        try:
            month = int(sys.argv[3])
        except ValueError:
            print("Please provide a valid month (1-12) for the summary.")
            sys.exit(1)
        if not 1 <= month <= 12:
            print("Please provide a month (1-12) for the summary.")
            sys.exit(1)
        if len(sys.argv) > 4:
            print("Please provide only one month (1-12) for the summary.")
            sys.exit(1)
        total_month = sum(expense["amount"] for expense in expenses if int(expense["date"].split("-")[1]) == month)
        if total_month == 0:
            print(f"No expenses found for month {month}...yet.")
        else:
            print(f"Total expenses for month {month}: ${total_month:.2f}")
        if total_month > 150:
            print(f"Warning: Your expenses for month {month} exceeds $150. No Ferrari for you!")
    else:
        print(f"Please use 'month' to get a monthly summary.")
        sys.exit(1)
else: 
    print("Invalid command. Please use: add, list, delete, update, summary")
    sys.exit(1)