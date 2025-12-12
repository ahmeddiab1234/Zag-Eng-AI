import json

expenses = []

def load_expenses(filename="expenses.json"):
    global expenses
    try:
        with open(filename, "r") as f:
            expenses = json.load(f)
    except FileNotFoundError:
        print("No previous expenses found, starting fresh.")
    except json.JSONDecodeError:
        print("File is corrupted, starting fresh.")



def save_expenses(filename="expenses.json"):
    with open(filename, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")
        expense = {"amount": amount, "category": category, "date": date}
        expenses.append(expense)
        print(f"Added expense: ${amount} for {category} on {date}")
    except ValueError:
        print("Invalid input, please enter a number for amount.")

def show_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    for e in expenses:
        print(f"${e['amount']} - {e['category']} on {e['date']}")

def summary_by_category():
    summary = {}
    for e in expenses:
        summary[e['category']] = summary.get(e['category'], 0) + e['amount']
    print("Summary by category:")
    for cat, total in summary.items():
        print(f"{cat}: ${total:.2f}")


"""

    {
        "amount": 25.5,
        "category": "Food",
        "date": "2025-12-01"
    },
    {
        "amount": 10.0,
        "category": "Transport",
        "date": "2025-12-01"
    },
    {
        "amount": 45.0,
        "category": "Food",
        "date": "2025-12-03"
    },


 summary = {}
    summary[Food] = 0 + 25.5 = 25.5
    summary[transport] = 0 + 10.0 = 10.0
    summary[Food] = 25.5 + 45.5 = 70.0
"""


if __name__ == "__main__":
    load_expenses()
    while True:
        print("\n1) Add expense\n" \
        "2) Show expenses\n" \
        "3) Summary by category" \
        "\n4) Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
            save_expenses()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            summary_by_category()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            
