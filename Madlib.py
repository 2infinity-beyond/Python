
"""
Name: Regina Stovall

                                    MADLIB Assignment
"""
# creating space before code block for visual cleanliness
print("\n")

#defining a function for making a custom song with 8 parameters
def custom_song(red,orange,adjective1,yellow,green,blue,adjective2,adjective3):

    # printing song lyrics with custom words/parameters

    print("\n") #print empty line to before song starts
    print("Let's sing a song about making a rainbow!...\n") 
    print(f"First, we have Red!\nIt's the color of a/an {red}.")
    print(f"Orange!\nIt's the color of a/an {orange}.")
    print(f"Yellow!\nIt's the color of the {adjective1} {yellow} {yellow} {yellow}!")
    print(f"Green!\nIt's the color of {green} and lots of things that grow!")
    print(f"Then there's Blue for the {blue}...")
    print(f"And Purple is a color that's {adjective2}, {adjective2}, {adjective2}!")
    print(f"And then we put those colors side by side, \nnow what do you think we've done?...")
    print(f"We've made a rainbow! -- \nAnd it's a really really {adjective3} one!")
    print("\n\n") #printing empty space at the end of the song

# setting function parameters to match invoked user inputs
red= input("Something that is red is a/an: ") 
orange = input("Something that is orange is a/an: ")
yellow = input("Something that is yellow is the: ")
adjective1 = input("Now using one word, describe it: ")
green = input("Something plural that is green is: ")
blue = input("Something that is blue is the: ")
adjective2 = input("Describe the color purple in one word: ")
adjective3 = input("Use one word to describe a rainbow: ")    

#calling the custom song function to generate lyrics using the custom parameters derived from the user inputs
custom_song(red,orange,adjective1,yellow,green,blue,adjective2,adjective3)