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

if sys.argv[1] == "add":
    expenses = load_expenses()
    highest_id = max(expense["id"] for expense in expenses) if expenses else 0
    new_expense = {
        "id": highest_id + 1,
        "description": sys.argv[2],
        "amount": float(sys.argv[3]),
        "date": timestamp
    }
    expenses.append(new_expense)
    print("Expense added to memory!")
    save_expenses(expenses)

if sys.argv[1] == "list":
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

if sys.argv[1] == "delete":
    expenses = load_expenses()
    expense_id = int(sys.argv[2])
    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            break
    print(f"Expense with ID: {expense_id} deleted!")
    save_expenses(expenses)