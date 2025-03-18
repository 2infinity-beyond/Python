'''
Homework21
Name: Regina Stovall
github link: https://github.com/2infinity-beyond/Python
'''

# function to check if a string is a palindrome
def is_palindrome(string):

    # create a new variable containing the string in reverse
    backwards_string = string[::-1]

    # if the reversed string is just like the original string, return True or False
    if backwards_string == string:
        return True
    else:
        return False
    pass
    
    # function to check if two strings are anagrams of each other
def is_anagram(string1,string2):

    # turning both strings into lists for ease of manipulation
    string1_list = list(string1) 
    string2_list = list(string2)
    
    # sorting each list into alphabetical order
    string1_list.sort()
    string2_list.sort()

    # if both lists are the same after sorting, return True or False
    if string1_list == string2_list:
        return True
    else:
        return False
    pass

    # defining the program's main function(s)
def main():
    is_palindrome()
    is_anagram()

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest21.py'))