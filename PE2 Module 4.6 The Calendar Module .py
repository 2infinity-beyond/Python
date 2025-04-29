'''
PE2 Module 4.6 The Calendar Module 
Name: Regina Stovall
github link: https://github.com/2infinity-beyond/Python
'''

import calendar
import datetime

# main function to process user input and output
def main():

    # getting the current year 
    current_year = datetime.datetime.now().year

    user_input_month = int(input("Please enter the number the corresponds with your birth month: "))
    
    # loop to ensure user input is within the appropriate boundaries
    # and handle any exceptions
    while True:
        try:
            if 1 <= user_input_month <= 12:
                break 
        
            else:
                print("Please enter a month number between 1 and 12")
        except ValueError:
            print("Invalid entry. Please try again...")

    # a calendar variable using the current year and user provided month
    birth_month = calendar.month(current_year, user_input_month)

    print(birth_month)

main()
