'''
Homework20
Name: Regina Stovall
github link: https://github.com/2infinity-beyond/Python
'''
# function to convert string characters to ascii values
def convert_to_ascii(string):

# for every character in the string:
    for char in string:
        # if the string contains only one character, simply output its ascii value
        if len(string) == 1:
            print(ord(char))
        # for all other strings, output the ascii value for all of its characters, 
        # separate the values with a comma  
        else:
            print(f"{ord(char)}", sep=", ", end=" ")    

 # function to filter out non-ascii characters from a string   
def filter_non_ascii(string):

    # for every character in the string:
    for char in string:

        # if the character is an ascii character: print it 
        if char.isascii():
            print(f"{char}", end="")
    pass

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest20.py'))