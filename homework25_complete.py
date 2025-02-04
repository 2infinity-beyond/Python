'''
Homework2.9
Name: Regina Stovall 
github link: 
'''

def budget(income,total_expenses,percentage):
    # your code here
    income = input("what is your monthly income?")
    print("Sounds good. Let's analyze your expenses for the month.")
    housing= input("How much do you pay for housing per month?")
    percentage_1 = float(housing / income)
    print("Your housing expense is ", percentage, "percent of your monthly budget.\n cont")
    # cont = ("Let's keep going...")
    utilities = input("How much do you pay for utilites per month?")
    percentage_2 = float(utilities / income)
    print("Your utilities expense is ", percentage, "percent of your monthly budget.\n cont)
    groceries = input("How much do you pay for groceries per month?")
    transportation = input("How much do you pay for transportation per month?")
    health_care = input("How much do you pay for health care per month?")
    personal_care = input("How much do you pay for personal care per month?")
    clothing_expense = input("How much do you pay for clothing per month?")
    debt_expense = input("What is the amount of debt you own?")
     

    ''' this function generates a personalized message 
    for the user based on the provided birthday'''

def address(street,city,state,zipcode):
    #your code here
    street = ("123 Main st") # user's street address
    city = ("Starfall") # user's city
    state = ("AZ") # user's state
    zipcode = (60547) # user's zipcode
    address = street, city, state, zipcode # user's complete address
    print("Your address is", address,".") 
    ''' this function generates a personalized message
    for the user based on the provided address''' 

