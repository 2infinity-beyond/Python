'''
PE2 Module 4.5 The DATETIME module 
Name: Regina Stovall
github link: https://github.com/2infinity-beyond/Python
'''

from datetime import datetime

def main():
    
    # starting a loop for error handling purposes
    while True: 

        # try-except block to test the datetime functions with the user provided parameters
        try:
            today = datetime.today()
            birth_year = int(input("\n\nWhat year were you born?  "))       
            month = int(input("What month were you born (as a number. May would be 5)  "))
            day = int(input("What day of the month were you born?  "))
        

            birthday = datetime(birth_year, month, day)
            print("\nYour Birthday is: ", end ='')
            
            # format the string of the datetime information 
            birthday_output = birthday.strftime("%Y-%m-%d")
            print(birthday_output) 

            
            delta = (today - birthday)
            print(f'\n   You are {delta.days:,} days young!')

            
            delta_years = int(delta.days / 365.2425)
            print(f'\n      You are {delta_years:,} years young!')

            
            # calculating the precise number of months 

            addtl_days = delta.days % 365.2425                   # get leftover days out of an incomplete year
            addtl_months = int(addtl_days / 30.44)               # convert those days into leftover months
            delta_months = delta_years * 12 + addtl_months       # get the total number of months by multiplying each year by 12
                                                                 # and adding it to the leftover months 
            print(f'\n          You are {delta_months:,} months young!')

             
            delta_weeks = int(delta.days / 7)
            print(f'\n              You are {delta_weeks:,} weeks young!')
            break    # stop loop 
        
        
        except ValueError as e:
            print(f"\nOh no! {e}. Please try again..") 
    
    # custom message at the end of the loop program
    print("\n                   - CONGRATULATIONS on making it this far! You Rock!! - \n\n")
        
main()
