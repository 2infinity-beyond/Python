'''
PE2 Modoule 3.6: Exceptions Again
Name: Regina Stovall
github link: https://github.com/2infinity-beyond/Python
'''
'''
Requirements
Implement a custom exception class NotNumericError.'''

# defining a custom sub-class of the exception class to catch non-numeric valueErrors
class NotNumericError(Exception):
    
    # initiating class and attributes
    def __init__(self, message = "\nUh-Oh! You did not enter a valid number..."):
        self.message = message

'''
Write a Python script that prompts the user to input a number.
Use a try-except-else-finally block: 

    The try block should contain the logic to check if the input is a number. (isnumeric() )
    The except block should catch the InvalidInputError and print an error message.
    The else block should print a confirmation message if the input is valid.
    The finally block should print a message indicating the end of the program's execution.

Ensure the program gracefully handles the exception and continues to prompt the user until a valid number is entered. (call the program again)
'''

# defining main function to check user input for non-numeric valueError 
def main():

    # setting a loop to continuously prompt user input until acceptable input is achieved   
    while True: 

        # try-except-else-finally block to check for input error and show custom exception message
        try:                             # logical operation to check if input is valid or leads to error
            user_input = input("\nPlease enter a valid number: ")
            if not user_input.isnumeric():  
                raise NotNumericError     # raise custom exception if error occurs
            else: 
                pass                      # move to next operation
        except NotNumericError as e:      # recall the custom exception message for the error  
            print(f"{e.message}")         # display the custom exception message to the user
        else:                             # if the input error is not present
            print(f"\nYou have successfully entered a valid number: {user_input}")    # confirm successful input to user
            break                         # now stop the loop
        finally:
            print("\n*operation completed*\n")  # program execution status to be printed each time

main()
