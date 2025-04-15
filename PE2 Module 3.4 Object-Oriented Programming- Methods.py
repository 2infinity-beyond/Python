'''
PE2 Module 3.4 Object-Oriented Programming- Methods
Name: Regina Stovall
github link: https://github.com/2infinity-beyond/Python
'''

'''Task Description:

#         Create the Pet Class:
#             Define a Pet class with attributes: kind (e.g., dog, cat), breed, and name.
#             Implement get and set methods for each of these attributes.
#             Add a method called print_details that prints the details of the pet.'''

# establishing a 'Pet' class
class Pet: 

    # initializing the class with the following attributes:
    def __init__(self, name, kind, breed):
        self._name = name
        self._kind = kind
        self._breed = breed
    
    # implementing 'get' and 'set' methods for class attributes   
    def getname(self):
        if hasattr(self, "_name"):
            return self._name
        
    def getkind(self):
        if hasattr(self,"_kind"):
            return self._kind
    
    def getbreed(self):
        if hasattr(self, "_breed"):
            return self._breed
    
    def setname(self, name):
        self._name = name

    def setkind(self, kind):
        self._kind = kind

    def setbreed(self, breed):
        self._breed = breed

    # implementing a method to print the object attributes in a custom format:  
    def print_details(self):
        print(f"Pet name: {self._name}\nPet kind: {self._kind}\nPet breed: {self._breed}\n")

'''         Create Instances:
#         Create three objects of the Pet class with different kinds, breeds, and names.'''

# creating three 'Pet' instances with defined attributes
pet1 = Pet ("Tricky", "turtle", "Snapping")
pet2 = Pet ("Bossy", "bunny", "Pigmy")
pet3 = Pet ("Riley", "robin", "American")

'''#         Call the print_details method for each object that you created'''
print("\n\n")
pet1.print_details()
pet2.print_details()
pet3.print_details()

'''        Demonstrate a Special Method or Function:

#         Choose one of the following and demonstrate its use with the Pet class instances:
#             __name__: Display the name of the class.
#             type(): Show the class used to instantiate a pet object.
#             __module__: Return the module name in which the Pet class is defined.
#             __bases__: Display the base classes of the Pet class (if any).
#             getattr(): Use it to access an attribute of a Pet instance.
#             isinstance(): Check if an instance is of the Pet class.'''

# demonstrating the usage of other special class methods and functions
print()
print(pet1._name)                 # using __name__ method
print(type(pet2))                 # using type() method
print(getattr(pet3, '_kind'))     # using getattr() method
print(isinstance(pet1, Pet))      # using isinstance()
print()

# testing 'get' method
print(pet2.getkind())           
print()

# testing the 'set' method
pet1.setbreed("Softshell")
print(pet1._breed)
print()

 