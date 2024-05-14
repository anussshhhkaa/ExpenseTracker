class Expense:
  """
  Represents a single expense with amount, description, and category.
  """
  def __init__(self, amount, description, category):
    self.amount = amount
    self.description = description
    self.category = category

class ExpenseTracker:
  """
  Tracks expenses with functionalities for adding, summarizing, and reporting.
  """
  def __init__(self):
    self.expenses = []
    self.load_expenses()  # Load expenses from file on initialization (optional)

  def add_expense(self, amount, description, category):
    """
    Adds a new expense to the tracker.
    """
    expense = Expense(amount, description, category)
    self.expenses.append(expense)
    self.save_expenses()  # Save expenses to file after adding (optional)

  def get_monthly_summary(self, month, year):
    """
    Calculates total expenses and category-wise breakdown for a given month and year.
    """
    monthly_expenses = [expense for expense in self.expenses if expense.date.month == month and expense.date.year == year]
    total_amount = sum(expense.amount for expense in monthly_expenses)
    category_totals = {}
    for expense in monthly_expenses:
      category_totals[expense.category] = category_totals.get(expense.category, 0) + expense.amount
    return total_amount, category_totals

  def print_report(self, month, year):
    """
    Prints a formatted report of total expenses and category breakdown for a month.
    """
    total_amount, category_totals = self.get_monthly_summary(month, year)
    print(f"Expense Report for {month}/{year}:")
    print(f"Total Expenses: ${total_amount:.2f}")
    if category_totals:
      print("\nCategory Breakdown:")
      for category, amount in category_totals.items():
        print(f"- {category}: ${amount:.2f}")
    else:
      print("No expenses found for this month.")

  def save_expenses(self):
    """
    Saves expense data to a file (implementation depends on chosen file format).
    """
    # Replace with your preferred file I/O method (e.g., JSON, CSV)
    with open("expenses.data", "w") as file:
      # Write data to the file in the chosen format
      pass

  def load_expenses(self):
    """
    Loads expense data from a file (implementation depends on chosen file format).
    """
    # Replace with your preferred file I/O method (e.g., JSON, CSV)
    try:
      with open("expenses.data", "r") as file:
        # Read data from the file and parse it into Expense objects
        pass
    except FileNotFoundError:
      # Handle the case where the file doesn't exist (optional)
      pass

# User Interface (replace with your preferred UI framework or text-based interaction)
def main():
  tracker = ExpenseTracker()
  while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Monthly Report")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
      amount = float(input("Enter amount: "))
      description = input("Enter description: ")
      category = input("Enter category (e.g., food, transportation): ")
      tracker.add_expense(amount, description, category)
      print("Expense added successfully!")
    elif choice == '2':
      month = int(input("Enter month (1-12): "))
      year = int(input("Enter year: "))
      tracker.print_report(month, year)
    elif choice == '3':
      print("Exiting Expense Tracker.")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
