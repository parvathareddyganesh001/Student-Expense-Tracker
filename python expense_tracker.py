
print("Welcome to Student Expense Tracker")

budget = int(input("Enter your monthly budget: "))

expenses = []

n = int(input("Enter number of expenses: "))

for i in range(n):
    amount = int(input("Enter expense amount: "))
    expenses.append(amount)

total = sum(expenses)

balance = budget - total

print("\n----- Expense Report -----")
print("Your Budget:", budget)
print("Your Expenses:", expenses)
print("Total Spending:", total)
print("Remaining Balance:", balance)

if balance < 0:
    print("You have crossed your budget.")
else:
    print("You are within your budget.")

print("Thank you!")
