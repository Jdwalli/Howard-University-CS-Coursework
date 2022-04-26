#prompt to enter monthly income
monthly_income = float(input("Enter your monthly income: "))

#prompt to enter rent
rent = float(input("Enter your rent: "))


#prompt to enter grocery expense
grocery_expense = float(input("Enter your grocery expense: "))


#prompt to enter internet bill
internet_bill = float(input("Enter your internet bill: "))

#prompt to enter cell phone bill 
cellphone_bill  = float(input("Enter your cell phone bill: "))

#prompt to enter the cost for personal subscriptions such as Netflix, Amazon, 
personal_subscriptions  = float(input("Enter your personal subscriptions: "))


#calculate per head expenses with shared bills 
rent_per_head = rent / 3
grocery_expense_per_head = grocery_expense / 3 
internet_bill_per_head = internet_bill / 3

#calculate total expenses 
total_monthly_expenses = rent_per_head + grocery_expense_per_head + internet_bill_per_head + cellphone_bill + personal_subscriptions

#calculate monthly saving and print it 2 decimal places.
monthly_savings = f"{monthly_income - total_monthly_expenses:.2f}"
print(monthly_savings)