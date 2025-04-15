'''
PE2 Module 3.5.1.1 OOP Fundamentals: Inheritance
Name: Regina Stovall
github link: https://github.com/2infinity-beyond/Python
'''

''' INSTRUCTIONS:
    File 1: Write an Employee class with the following attributes:
    Employee name
    Employee number'''

'''Implement accessor and mutator methods (getters and setters) for each class'''

#defining Employee class with attributes for name and ID number
class Employee:

    #initializing class with employee attributes 
    def __init__(self, fname, lname, number):
        self.fname = fname
        self.lname = lname
        self.number = number
    
    # implementing getter and setter methods for each attribute
    def setfname(self, fname):
        self.fname = fname
        
    def getfname(self):
        if hasattr (self, "fname"):
            return self.fname

    def setlname(self, lname):
        self.lname = lname
    
    def getlname(self):
        if hasattr (self, "lname"):
            return self.lname
        
    def setnumber(self, number):
        self.number = number
    
    def getnumber(self):
        if hasattr (self, "_number"):
            return self.number

    # implementing string method to establish a custom string representation for class object attributes
    def __str__(self):
        return f"\n\nEMPLOYEE DETAILS:\n\nEmployee Name: {self.lname}, {self.fname}\nID Number: {self.number}\n"
        pass

'''Create a subclass named ProductionWorker that inherits from Employee. This subclass should include additional attributes:

    Shift number (integer: 1 for day, 2 for night)
    Hourly pay rate'''

'''Implement accessor and mutator methods (getters and setters) for each class'''

# creating sub-class of Employee called 'ProductionWorker' 
class ProductionWorker(Employee):

    #initializing the class with its attributes
    def __init__(self, fname, lname, number, shift, pay):

        # calling the initializer of the parent class for the common attributes
        super().__init__(fname, lname, number)

        # setting additional attributes specific to this sub-class
        self.setshift(shift)
        self.pay = pay

    # implementing getter and setter methods for class attributes
    def setshift(self, shift):
        if shift in [1, 2]:
            self.shift = "Day" if shift == 1 else "Night"     # shift code 1 for Day, 2 for Night
        else:
            raise ValueError ("Error: Enter 1 for Day shift or 2 for Night shift")
        
    def getshift(self):
        if hasattr (self, "shift"):    
            return self.shift
        
    def setpay(self, pay):
        self.pay = pay
    
    def getpay(self):
        if hasattr (self, "pay"):
          return self.pay
        
    # string method to display class object attributes
    def __str__(self):
        return super().__str__() +f"Shift: {self.getshift()}\nHourly Pay Rate: ${self.pay:.2f}\n" 
       

'''Assignment Part 2: Implementing and Testing

# Part 2: Write a script to
#         Create an instance of ProductionWorker
#         Prompt the user for each attribute's data. 
#         Store and then display the data using the object's methods.'''

# establishing a main function to pass its data through the class functions
def main():

    # prompting user for attribute data
    print()
    fname = input("Enter Employee first name: ")
    lname = input("Enter Employee last name: ")
    number = input("Enter Employee ID number: ")
    shift = int(input("Enter shift code: "))
    pay = float(input("Enter hourly pay rate: "))
    
    # creating an instance of ProductionWorker class with attribute information from user inputs
    worker1 = ProductionWorker(fname, lname, number, shift, pay)

    # printing the object information using the class' string method defined within the class
    print(worker1)

# calling main function to initiate user input prompts to collect and process the data according to class functions 
main()
    


