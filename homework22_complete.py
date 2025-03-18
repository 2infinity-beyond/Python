'''
Homework22
Name: Regina Stovall
github link: https://github.com/2infinity-beyond/Python
'''

# defining a function to mask credit card numbers, only revealing the last four 
def mask_creditcard(string):

    # creating a variable that contains the formula for masking card numbers
    # the number of asterisks needed for concealment is four less than the total numbers on the card
    # add the last four numbers from the card to the variable using the slice method 
    masked_digits = "*" * (len(string) - 4) + string[-4:]
    print(f"'{masked_digits}'")    
    pass
    

    # defining a function to remove the vowels from strings
def remove_vowels(string):

    #convert the string to a list for ease of manipulation
    string_list = list(string)

    # store all the vowels that will be tested in a separate variable
    vowels = "aeiouAEIOU"

    # convert vowels to a list for ease of manipulation
    vowel_list = list(vowels)

    # for every item in the string list:
    for i in string_list:

        # check every vowel. If there is one in the string list, remove it
        for vowel in vowel_list:
            if vowel in string_list:
                string_list.remove(vowel)
    
    # create a new string containing the new string list with no vowels
    new_string= "".join(string_list)

    # print the new string
    print(f"'{new_string}'")

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest22.py'))