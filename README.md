# Expense_TrackerCLI
Track your expenses through command!
# Expense Tracker CLI

A simple command-line expense tracker built with Python as part of the **roadmap.sh Expense Tracker** project.

🔗 **Project Specification:**
https://roadmap.sh/projects/expense-tracker

This application allows users to manage personal expenses directly from the terminal. Expenses are stored locally in a JSON file and can be added, updated, deleted, listed, and summarized.

---

## Features

* ✅ Add new expenses
* ✅ List all expenses
* ✅ Update existing expenses
* ✅ Delete expenses
* ✅ View total expenses
* ✅ View monthly expense summaries
* ✅ Automatic expense ID generation
* ✅ Persistent JSON storage
* ✅ Input validation and helpful error messages
* ✅ Graceful handling of missing or corrupted `expenses.json`
* ✅ Fun spending warning when monthly expenses exceed **$150**

---

## Technologies Used

* Python 3
* JSON
* Command Line Interface (CLI)

No external libraries are required.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Expense_TrackerCLI.git
cd Expense_TrackerCLI
```

Run the application directly:

```bash
python expenses.py
```

The application automatically creates an empty expense list if `expenses.json` does not exist or is invalid.

---

## Usage

### Add an Expense

```bash
python expenses.py add "Lunch" 12.50
```

Output:

```text
Expense added to memory!
```

---

### List All Expenses

```bash
python expenses.py list
```

Example:

```text
ID   Date        Description       Amount
1    2026-06-26  Lunch             $12.50
2    2026-06-26  Coffee            $4.25
```

---

### Update an Expense

```bash
python expenses.py update 1 "Dinner" 18.75
```

Output:

```text
Expense with ID: 1 updated!
```

---

### Delete an Expense

```bash
python expenses.py delete 1
```

Output:

```text
Expense with ID: 1 deleted!
```

---

### View Total Expenses

```bash
python expenses.py summary
```

Example:

```text
Total expenses: $152.50
Don't forget to save and invest!
```

---

### View Monthly Summary

```bash
python expenses.py summary month 6
```

Example:

```text
Total expenses for month 6: $87.50
```

If no expenses are found:

```text
No expenses found for month 6...yet.
```

If expenses exceed **$150**:

```text
Warning: Your expenses for month 6 exceeds $150.
No Ferrari for you!
```

---

## Project Structure

```text
Expense_TrackerCLI/
│
├── expenses.py
├── expenses.json
└── README.md
```

---

## Expense Data Format

Expenses are stored in `expenses.json` as a list of objects.

Example:

```json
[
    {
        "id": 1,
        "description": "Lunch",
        "amount": 12.5,
        "date": "2026-06-26"
    }
]
```

---

## Error Handling

The application validates user input and handles common errors, including:

* Missing commands
* Invalid commands
* Missing arguments
* Invalid expense IDs
* Invalid amounts
* Invalid month values
* Too many command-line arguments
* Missing `expenses.json`
* Corrupted or empty JSON files

---

## Python Concepts Practiced

This project reinforced several core Python concepts:

* Functions
* Lists and dictionaries
* CRUD operations
* JSON serialization and deserialization
* File handling
* Command-line argument parsing (`sys.argv`)
* Exception handling (`try` / `except`)
* Generator expressions
* Built-in functions (`sum()`, `max()`)
* Input validation
* Program flow using `if`, `elif`, and `else`
* Working with dates using `datetime`

---

## Future Improvements

Some possible future enhancements include:

* Expense categories
* Budget tracking
* CSV export
* Search expenses
* Support for multi-word descriptions without quotation marks
* Better command parsing using `argparse`
* Database storage (SQLite or PostgreSQL)

---

## Acknowledgements

This project was built by following the **Expense Tracker** project idea from roadmap.sh.

Project page:

https://roadmap.sh/projects/expense-tracker

---

## License

This project is released under the MIT License.
