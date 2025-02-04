'''
Homework2.9
Name: Regina Stovall 
github link: 
'''

# this basic budget program will help user's see how much of their income is going towards their expenses

print("Let's Budget!") # Introduction to the user
    
income = input("what is your total monthly income?") # Collect user's starting income for the month
print("Sounds good. Let's analyze your expenses for the month.\n") 

housing_expense= input("How much do you pay for housing per month?") # user must input numerical data
cont = ("Let's keep going...\n\n") # variable statement will be reused throughout program as a user-friendly transitional statement
percentage_1 = float(housing_expense) / float(income) # calculating percentage of income for each expense as we go

print(f"Your housing expense is {percentage_1:.2f} percent of your monthly budget.\n\n", cont) # output percentage

utilities_expense = input("Now, how much do you pay for utilites per month?") # user must input numerical data
percentage_2 = float(utilities_expense) / float(income) # calculating percentage of income for each expense as we go
print(f"Your utilities expense is {percentage_2:.2f} percent of your monthly budget.\n\n", cont) # output percentage

groceries_expense = input("How much do you pay for groceries per month?") # user must input numerical data
percentage_3 = float(groceries_expense) / float(income) # calculating percentage of income for each expense as we go
print(f"Your groceries expense is {percentage_3:.2f} percent of your monthly budget.\n\n", cont) # output percentage

transportation_expense = input("Now what about transportation?\nHow much do you pay for transportation per month?") # user must input numerical data
percentage_4 = float(transportation_expense) / float(income) # calculating percentage of income for each expense as we go
print(f"Your transportation expense is {percentage_4:.2f} percent of your monthly budget.\n\n", cont) # output percentage

health_care_expense = input("Do you pay for health care? If so, how much per month?") # user must input numerical data
percentage_5 = float(health_care_expense) / float(income) # calculating percentage of income for each expense as we go
print(f"Your health care is {percentage_5:.2f} percent of your monthly budget. \n\n", cont) # output percentage

personal_care_expense = input("Now how much do you pay for personal care per month?") # user must input numerical data
percentage_6 = float(personal_care_expense) / float(income) # calculating percentage of income for each expense as we go
print(f"Your personal care is {percentage_6:.2f} percent of your monthly budget.\n\n", cont) # output percentage

clothing_expense = input("What's the typical amount you would spend on clothing per month?") # user must input numerical data
percentage_7 = float(clothing_expense) / float(income) # calculating percentage of income for each expense as we go
print(f"Your clothing expense is {percentage_7:.2f} percent of your monthly budget\n\n", cont) # output percentage

debt_expense = input("Last, but not least, how much do you pay monthly towards debts that you owe?") # user must input numerical data
percentage_8 = float(debt_expense)/ float(income) # calculating percentage of budget for each expense as we go
print(f"Your debt is {percentage_8:.2f} percent of your monthly budget.\n\n") # output percentage
     
acceptable_budget = input("Now that we've calculated everything, press enter to see your total monthly expenses.") # time for the total expense liability
# below we calculate the total percentage of the income for all expenses combined
total_expenses = (float(housing_expense) + float(utilities_expense) + float(groceries_expense)+ float(transportation_expense) + float(health_care_expense) + float(personal_care_expense) + float(clothing_expense) + float(debt_expense)) / float(income)
print(f"Your total monthly expenses are {total_expenses:.2f} percent of your monthly income.\n\n") # output percentage                     

